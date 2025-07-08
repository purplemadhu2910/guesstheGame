function submitGuess() {
    const guess = document.getElementById('guess').value;

    fetch('/guess', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ guess: guess })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('feedback').innerText = data.feedback;
    })
    .catch(error => console.error('Error:', error));
}

function restartGame() {
    document.getElementById('feedback').innerText = "Game restarted! Make a new guess.";
    document.getElementById('guess').value = "";
}
