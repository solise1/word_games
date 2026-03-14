const board = document.getElementById('board');
const form = document.getElementById('guess-form');
const input = document.getElementById('guess-input');
const message = document.getElementById('message');

let guesses = [];
let evaluations = [];
let gameOver = false;

function renderBoard() {
    board.innerHTML = '';
    for (let i = 0; i < maxGuesses; i++) {
        const row = document.createElement('div');
        row.className = 'row';
        let guess = guesses[i] || '';
        let evaluation = evaluations[i] || [];
        for (let j = 0; j < 5; j++) {
            const cell = document.createElement('div');
            cell.className = 'cell';
            if (guess[j]) {
                cell.textContent = guess[j];
                if (evaluation[j]) {
                    cell.classList.add(evaluation[j]);
                }
            }
            row.appendChild(cell);
        }
        board.appendChild(row);
    }
}
form.onsubmit = async function(e) {
    e.preventDefault();
    if (gameOver) return;
    const guess = input.value.toUpperCase();
    if (guess.length !== 5) return;

    // Send guess to backend
    const response = await fetch('/guess/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ guess })
    });
    const data = await response.json();
    guesses.push(guess);
    evaluations.push(data.evaluation);
    renderBoard();
    input.value = '';
    if (data.is_correct) {
        message.textContent = 'Congratulations! You guessed the word!';
        gameOver = true;
    } else if (guesses.length === maxGuesses) {
        message.textContent = 'Game over! The word was ' + data.solution + '.';
        gameOver = true;
    }
};
renderBoard();
