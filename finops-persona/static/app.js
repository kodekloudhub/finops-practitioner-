let pairs = [];
let shuffledResponsibilities = [];
let draggedPersona = null;
let usedPersonas = new Set();
let usedResponsibilities = new Set();

function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/pairs')
        .then(res => res.json())
        .then(data => {
            pairs = data;
            resetGame();
        });

    document.getElementById('reset-btn').addEventListener('click', resetGame);
});

function renderGame() {
    const personasDiv = document.getElementById('personas');
    const responsibilitiesDiv = document.getElementById('responsibilities');
    
    personasDiv.innerHTML = '<h2>Personas</h2>';
    responsibilitiesDiv.innerHTML = '<h2>Responsibilities</h2>';

    pairs.forEach(pair => {
        if (!usedPersonas.has(pair.persona)) {
            const pDiv = document.createElement('div');
            pDiv.className = 'draggable persona';
            pDiv.textContent = pair.persona;
            pDiv.draggable = true;
            pDiv.addEventListener('dragstart', dragStart);
            personasDiv.appendChild(pDiv);
        }
    });

    shuffledResponsibilities.forEach(responsibility => {
        const rDiv = document.createElement('div');
        rDiv.className = 'droppable responsibility';
        rDiv.textContent = responsibility;
        if (usedResponsibilities.has(responsibility)) {
            rDiv.classList.add('disabled');
        } else {
            rDiv.addEventListener('dragover', dragOver);
            rDiv.addEventListener('drop', drop);
        }
        responsibilitiesDiv.appendChild(rDiv);
    });
}

function resetGame() {
    shuffledResponsibilities = pairs.map(p => p.responsibility);
    shuffle(shuffledResponsibilities);
    usedPersonas = new Set();
    usedResponsibilities = new Set();
    renderGame();
    document.getElementById('feedback').textContent = '';
}

function dragStart(e) {
    draggedPersona = e.target.textContent;
}

function dragOver(e) {
    e.preventDefault();
}

function drop(e) {
    e.preventDefault();
    const responsibility = e.target.textContent;
    checkMatch(draggedPersona, responsibility, e.target);
}

function checkMatch(persona, responsibility, targetDiv) {
    fetch('/api/check', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ persona, responsibility })
    })
    .then(res => res.json())
    .then(result => {
        usedPersonas.add(persona);
        usedResponsibilities.add(responsibility);

        if (result.result === 'correct') {
            targetDiv.classList.add('correct');
            targetDiv.textContent = `${responsibility} ✓`;
            showFeedback('Correct!');
        } else {
            targetDiv.classList.add('incorrect');
            showFeedback(`Incorrect! The correct answer is: ${result.correct_answer}`);
        }
        renderGame(); // re-render to remove used persona and responsibility
    });
}

function showFeedback(msg) {
    const feedback = document.getElementById('feedback');
    feedback.textContent = msg;
    setTimeout(() => { feedback.textContent = ''; }, 2000);
}