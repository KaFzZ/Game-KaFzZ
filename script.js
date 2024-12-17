let currentCard;
let nextCard;
let score = 0;

function getRandomCard() {
    return Math.floor(Math.random() * 13) + 1; // Cards from 1 to 13
}

function startGame() {
    currentCard = getRandomCard();
    document.getElementById('current-card').textContent = currentCard;
    document.getElementById('result').textContent = '';
}

function guess(playerGuess) {
    nextCard = getRandomCard();
    const resultDiv = document.getElementById('result');
    const scoreDiv = document.getElementById('score');

    if ((playerGuess === 'higher' && nextCard > currentCard) || 
        (playerGuess === 'lower' && nextCard < currentCard)) {
        resultDiv.textContent = `You guessed right! The next card was ${nextCard}.`;
        score++;
    } else {
        resultDiv.textContent = `You guessed wrong! The next card was ${nextCard}.`;
        score = Math.max(0, score - 1); // Prevent negative score
    }

    scoreDiv.textContent = `Score: ${score}`;
    currentCard = nextCard; // Update current card
    document.getElementById('current-card').textContent = currentCard; // Show new current card
}

// Start the game when the page loads
window.onload = startGame;
