document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/flipcards')
        .then(res => res.json())
        .then(cards => {
            const container = document.getElementById('flipcards-container');
            cards.forEach((card, idx) => {
                const cardDiv = document.createElement('div');
                cardDiv.className = 'flip-card';
                // Assign color class based on index
                const colorClass = `color-${idx % 10}`;
                cardDiv.innerHTML = `
                    <div class="flip-card-inner">
                        <div class="flip-card-front ${colorClass}">${card.front}</div>
                        <div class="flip-card-back">${card.back}</div>
                    </div>
                `;
                cardDiv.addEventListener('click', () => {
                    cardDiv.classList.toggle('flipped');
                });
                container.appendChild(cardDiv);
            });
        });
}); 