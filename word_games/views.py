from django.shortcuts import render
from django.utils.translation import get_language
from .settings import LANGUAGES

def change_language(request):
    languages = dict(LANGUAGES)

    return render(request, 'language.html', context={ 'languages': languages })
