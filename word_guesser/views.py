import json

from django.shortcuts import render
from django.http import JsonResponse
from . import WordGuesser
from django.views.decorators.csrf import csrf_exempt
from collections import Counter


MAX_GUESSES = 6

def get_solution(request):
    # ! Remove hardcoding of language and get locale or something
    language = 'english'
    # ! Remove hardcoding of language and get locale or something
    solution = request.session.get('solution')

    if not solution:
        solution = WordGuesser(language).pick_random().upper()
        request.session['solution'] = solution

    return solution


def word_guesser(request):
    # Clear the session
    request.session.flush()
    # Setup
    get_solution(request)
    request.session['guesses'] = []
    return render(request, 'word_guesser/index.html', context={ 'max_guesses': MAX_GUESSES})


@csrf_exempt
def guess(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

    data = json.loads(request.body)

    guess = data.get('guess', '').upper()

    if len(guess) != 5:
        return JsonResponse({'error': 'Invalid request'}, status=400)

    solution = get_solution(request)
    is_correct = guess == solution

    if is_correct:
        evaluation = ['correct'] * 5
        return JsonResponse({'evaluation': evaluation, 'is_correct': is_correct, 'solution': solution})

    guesses = request.session.get('guesses')
    guesses.append(guess)
    request.session['guesses'] = guesses

    out_of_guesses = len(guesses) >= MAX_GUESSES

    evaluation = evaluate_guess(list(guess), list(solution))

    return JsonResponse({'evaluation': evaluation, 'is_correct': is_correct, 'solution': solution if out_of_guesses else None})


def evaluate_guess(guess_chars, solution_chars):
    evaluation = ['absent'] * 5

    for i in range(5):
        if guess_chars[i] == solution_chars[i]:
            evaluation[i] = 'correct'
            solution_chars[i] = None
            guess_chars[i] = None

    remaining = Counter([c for c in solution_chars if c is not None])

    for i in range(5):
        if guess_chars[i] is not None and remaining[guess_chars[i]] > 0:
            evaluation[i] = 'present'
            remaining[guess_chars[i]] -= 1

    return evaluation
