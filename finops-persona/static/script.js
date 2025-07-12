 // Game state
let gameState = {
    problems: [],
    personas: [],
    selectedProblem: null,
    selectedPersona: null,
    matches: {},
    score: 0,
    completedProblems: new Set(),
    currentMission: null
};

// API base URL
const API_BASE = 'http://localhost:8002/api';

// DOM elements
const screens = {
    start: document.getElementById('start-screen'),
    game: document.getElementById('game-screen'),
    mission: document.getElementById('mission-screen'),
    results: document.getElementById('results-screen')
};

// Initialize the game
document.addEventListener('DOMContentLoaded', function() {
    initializeGame();
    setupEventListeners();
});

async function initializeGame() {
    try {
        // Load game data
        const [problemsResponse, personasResponse] = await Promise.all([
            fetch(`${API_BASE}/problems`),
            fetch(`${API_BASE}/personas`)
        ]);
        
        gameState.problems = (await problemsResponse.json()).problems;
        gameState.personas = (await personasResponse.json()).personas;
        
        renderProblems();
        renderPersonas();
    } catch (error) {
        console.error('Failed to initialize game:', error);
        showError('Failed to load game data. Please refresh the page.');
    }
}

function setupEventListeners() {
    // Start screen
    document.getElementById('start-game-btn').addEventListener('click', startGame);
    
    // Game screen
    document.getElementById('check-matches-btn').addEventListener('click', checkMatches);
    document.getElementById('reset-game-btn').addEventListener('click', resetGame);
    
    // Mission screen
    document.getElementById('submit-mission-btn').addEventListener('click', submitMission);
    document.getElementById('skip-mission-btn').addEventListener('click', skipMission);
    
    // Results screen
    document.getElementById('play-again-btn').addEventListener('click', playAgain);
    document.getElementById('back-to-start-btn').addEventListener('click', backToStart);
    
    // Modal
    document.getElementById('continue-btn').addEventListener('click', closeModal);
    document.querySelector('.close').addEventListener('click', closeModal);
    
    // Close modal when clicking outside
    window.addEventListener('click', function(event) {
        const modal = document.getElementById('feedback-modal');
        if (event.target === modal) {
            closeModal();
        }
    });
}

function renderProblems() {
    const container = document.getElementById('problems-container');
    container.innerHTML = '';
    
    gameState.problems.forEach(problem => {
        const problemCard = document.createElement('div');
        problemCard.className = 'problem-card';
        problemCard.dataset.problemId = problem.id;
        
        if (gameState.completedProblems.has(problem.id)) {
            problemCard.classList.add('matched');
        }
        
        problemCard.innerHTML = `
            <h4>${problem.title}</h4>
            <p>${problem.description}</p>
        `;
        
        problemCard.addEventListener('click', () => selectProblem(problem.id));
        container.appendChild(problemCard);
    });
}

function renderPersonas() {
    const container = document.getElementById('personas-container');
    container.innerHTML = '';
    
    gameState.personas.forEach(persona => {
        const personaCard = document.createElement('div');
        personaCard.className = 'persona-card';
        personaCard.dataset.personaName = persona.name;
        
        // Check if this persona is already matched
        const isMatched = Object.values(gameState.matches).includes(persona.name);
        if (isMatched) {
            personaCard.classList.add('matched');
        }
        
        personaCard.innerHTML = `
            <h4>${persona.name}</h4>
            <span class="persona-type ${persona.type.toLowerCase()}">${persona.type}</span>
            <p>${persona.description}</p>
        `;
        
        personaCard.addEventListener('click', () => selectPersona(persona.name));
        container.appendChild(personaCard);
    });
}

function selectProblem(problemId) {
    // Clear previous selections
    document.querySelectorAll('.problem-card.selected').forEach(card => {
        card.classList.remove('selected');
    });
    
    // Select new problem
    const problemCard = document.querySelector(`[data-problem-id="${problemId}"]`);
    if (problemCard && !gameState.completedProblems.has(problemId)) {
        problemCard.classList.add('selected');
        gameState.selectedProblem = problemId;
    }
    
    updateCheckButton();
}

function selectPersona(personaName) {
    // Clear previous selections
    document.querySelectorAll('.persona-card.selected').forEach(card => {
        card.classList.remove('selected');
    });
    
    // Check if persona is already matched
    const isMatched = Object.values(gameState.matches).includes(personaName);
    if (isMatched) return;
    
    // Select new persona
    const personaCard = document.querySelector(`[data-persona-name="${personaName}"]`);
    if (personaCard) {
        personaCard.classList.add('selected');
        gameState.selectedPersona = personaName;
    }
    
    updateCheckButton();
}

function updateCheckButton() {
    const checkBtn = document.getElementById('check-matches-btn');
    checkBtn.disabled = !(gameState.selectedProblem && gameState.selectedPersona);
}

async function checkMatches() {
    if (!gameState.selectedProblem || !gameState.selectedPersona) return;
    
    try {
        const response = await fetch(`${API_BASE}/match`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                problem_id: gameState.selectedProblem,
                persona_name: gameState.selectedPersona
            })
        });
        
        const result = await response.json();
        
        // Update game state
        gameState.matches[gameState.selectedProblem] = gameState.selectedPersona;
        gameState.score += result.score;
        
        if (result.correct) {
            gameState.completedProblems.add(gameState.selectedProblem);
        }
        
        // Show feedback
        showFeedback(result);
        
        // Update UI
        updateScore();
        updateProgress();
        renderProblems();
        renderPersonas();
        
        // Clear selections
        gameState.selectedProblem = null;
        gameState.selectedPersona = null;
        document.querySelectorAll('.problem-card.selected, .persona-card.selected').forEach(card => {
            card.classList.remove('selected');
        });
        updateCheckButton();
        
        // Check if game is complete
        if (gameState.completedProblems.size === gameState.problems.length) {
            setTimeout(() => {
                showResults();
            }, 2000);
        }
        
    } catch (error) {
        console.error('Failed to check match:', error);
        showError('Failed to validate match. Please try again.');
    }
}

function showFeedback(result) {
    const modal = document.getElementById('feedback-modal');
    const title = document.getElementById('feedback-title');
    const message = document.getElementById('feedback-message');
    const explanation = document.getElementById('feedback-explanation');
    
    if (result.correct) {
        title.textContent = '✅ Correct Match!';
        title.className = 'feedback-correct';
        message.textContent = `Great job! You correctly matched the problem to ${result.correct_persona}.`;
    } else {
        title.textContent = '❌ Incorrect Match';
        title.className = 'feedback-incorrect';
        message.textContent = `The correct persona for this problem is ${result.correct_persona}.`;
    }
    
    explanation.textContent = result.explanation;
    
    modal.style.display = 'block';
    
    // If correct, offer mini-mission
    if (result.correct) {
        const continueBtn = document.getElementById('continue-btn');
        continueBtn.textContent = 'Continue to Mini-Mission';
        continueBtn.onclick = () => {
            closeModal();
            showMiniMission(gameState.selectedProblem);
        };
    } else {
        const continueBtn = document.getElementById('continue-btn');
        continueBtn.textContent = 'Continue';
        continueBtn.onclick = closeModal;
    }
}

async function showMiniMission(problemId) {
    try {
        const response = await fetch(`${API_BASE}/mini-mission/${problemId}`);
        const data = await response.json();
        
        gameState.currentMission = {
            problemId: problemId,
            ...data.mission
        };
        
        // Populate mission screen
        document.getElementById('mission-title').textContent = data.mission.title;
        document.getElementById('mission-question').textContent = data.mission.question;
        
        const optionsContainer = document.getElementById('mission-options');
        optionsContainer.innerHTML = '';
        
        data.mission.options.forEach(option => {
            const optionDiv = document.createElement('div');
            optionDiv.className = 'mission-option';
            optionDiv.innerHTML = `
                <input type="radio" name="mission-option" value="${option.id}" id="option-${option.id}">
                <label for="option-${option.id}">${option.text}</label>
            `;
            
            optionDiv.addEventListener('click', () => selectMissionOption(option.id));
            optionsContainer.appendChild(optionDiv);
        });
        
        // Show mission screen
        showScreen('mission');
        
    } catch (error) {
        console.error('Failed to load mini-mission:', error);
        showError('Failed to load mini-mission. Continuing to next problem.');
    }
}

function selectMissionOption(optionId) {
    // Clear previous selections
    document.querySelectorAll('.mission-option.selected').forEach(option => {
        option.classList.remove('selected');
    });
    
    // Select new option
    const optionDiv = document.querySelector(`[value="${optionId}"]`).closest('.mission-option');
    optionDiv.classList.add('selected');
    
    // Update submit button
    document.getElementById('submit-mission-btn').disabled = false;
}

async function submitMission() {
    if (!gameState.currentMission) return;
    
    const selectedOption = document.querySelector('input[name="mission-option"]:checked');
    if (!selectedOption) return;
    
    try {
        const response = await fetch(`${API_BASE}/mini-mission/${gameState.currentMission.problemId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                problem_id: gameState.currentMission.problemId,
                selected_option: selectedOption.value
            })
        });
        
        const result = await response.json();
        
        // Update score
        gameState.score += result.score;
        updateScore();
        
        // Show feedback
        showMissionFeedback(result);
        
    } catch (error) {
        console.error('Failed to submit mission:', error);
        showError('Failed to submit mission answer. Please try again.');
    }
}

function showMissionFeedback(result) {
    const modal = document.getElementById('feedback-modal');
    const title = document.getElementById('feedback-title');
    const message = document.getElementById('feedback-message');
    const explanation = document.getElementById('feedback-explanation');
    
    if (result.correct) {
        title.textContent = '🎯 Mission Accomplished!';
        title.className = 'feedback-correct';
        message.textContent = 'Great job! You chose the correct action.';
    } else {
        title.textContent = '❌ Mission Failed';
        title.className = 'feedback-incorrect';
        message.textContent = 'That wasn\'t the best choice.';
    }
    
    explanation.textContent = result.explanation;
    
    modal.style.display = 'block';
    
    const continueBtn = document.getElementById('continue-btn');
    continueBtn.textContent = 'Continue';
    continueBtn.onclick = () => {
        closeModal();
        showScreen('game');
    };
}

function skipMission() {
    showScreen('game');
}

function updateScore() {
    document.getElementById('current-score').textContent = gameState.score;
}

function updateProgress() {
    document.getElementById('progress').textContent = `${gameState.completedProblems.size}/${gameState.problems.length}`;
}

function showResults() {
    // Calculate final score
    const maxScore = gameState.problems.length * 15; // 10 for match + 5 for mission
    document.getElementById('final-score').textContent = gameState.score;
    document.getElementById('max-score').textContent = maxScore;
    
    // Generate score breakdown
    const breakdownContainer = document.getElementById('score-breakdown');
    breakdownContainer.innerHTML = '';
    
    gameState.problems.forEach(problem => {
        const isCompleted = gameState.completedProblems.has(problem.id);
        const matchScore = isCompleted ? 10 : 0;
        const missionScore = isCompleted ? 5 : 0; // Assuming all completed problems had missions
        
        const breakdownItem = document.createElement('div');
        breakdownItem.className = 'score-breakdown-item';
        breakdownItem.innerHTML = `
            <span>${problem.title}</span>
            <span>${matchScore + missionScore} pts</span>
        `;
        breakdownContainer.appendChild(breakdownItem);
    });
    
    // Load learning outcomes
    loadLearningOutcomes();
    
    // Generate match summary
    generateMatchSummary();
    
    showScreen('results');
}

async function loadLearningOutcomes() {
    try {
        const response = await fetch(`${API_BASE}/game-summary`);
        const data = await response.json();
        
        const outcomesContainer = document.getElementById('learning-outcomes');
        outcomesContainer.innerHTML = '';
        
        data.learning_outcomes.forEach(outcome => {
            const li = document.createElement('li');
            li.textContent = outcome;
            outcomesContainer.appendChild(li);
        });
    } catch (error) {
        console.error('Failed to load learning outcomes:', error);
    }
}

function generateMatchSummary() {
    const summaryContainer = document.getElementById('matches-summary');
    summaryContainer.innerHTML = '';
    
    gameState.problems.forEach(problem => {
        const matchedPersona = gameState.matches[problem.id];
        const isCorrect = matchedPersona === problem.correct_persona;
        
        const summaryItem = document.createElement('div');
        summaryItem.className = `match-summary-item ${isCorrect ? '' : 'incorrect'}`;
        summaryItem.innerHTML = `
            <strong>${problem.title}</strong><br>
            <span>Your match: ${matchedPersona || 'Not matched'}</span><br>
            <span>Correct: ${problem.correct_persona}</span>
        `;
        summaryContainer.appendChild(summaryItem);
    });
}

function showScreen(screenName) {
    // Hide all screens
    Object.values(screens).forEach(screen => {
        screen.classList.remove('active');
    });
    
    // Show target screen
    screens[screenName].classList.add('active');
}

function startGame() {
    showScreen('game');
    updateScore();
    updateProgress();
}

function resetGame() {
    gameState = {
        problems: gameState.problems,
        personas: gameState.personas,
        selectedProblem: null,
        selectedPersona: null,
        matches: {},
        score: 0,
        completedProblems: new Set(),
        currentMission: null
    };
    
    renderProblems();
    renderPersonas();
    updateScore();
    updateProgress();
    updateCheckButton();
}

function playAgain() {
    resetGame();
    showScreen('game');
}

function backToStart() {
    resetGame();
    showScreen('start');
}

function closeModal() {
    document.getElementById('feedback-modal').style.display = 'none';
}

function showError(message) {
    alert(message); // Simple error handling - could be enhanced with a proper error modal
}