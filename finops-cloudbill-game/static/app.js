let currentBill = null;
let userCategories = {};
let userOptimizations = {};

const billSection = document.getElementById('bill-section');
const categorizationSection = document.getElementById('categorization-section');
const optimizationSection = document.getElementById('optimization-section');
const resultsSection = document.getElementById('results-section');
const tipSection = document.getElementById('tip-section');
const restartBtn = document.getElementById('restart-btn');

const categories = ['idle', 'underprovisioned', 'overprovisioned'];
const optimizations = ['rightsizing', 'lifecycle policy', 'release', 'no action'];

async function fetchBill() {
  const res = await fetch('/api/bill');
  const data = await res.json();
  currentBill = data;
  renderBill(data.items);
  tipSection.innerHTML = '';
  resultsSection.style.display = 'none';
  restartBtn.style.display = 'none';
}

function renderBill(items) {
  let html = '<h3>Step 1: Categorize Each Line Item</h3>';
  html += '<table><tr><th>Resource</th><th>Description</th><th>Cost ($)</th><th>Category</th><th>Feedback</th></tr>';
  items.forEach(item => {
    html += `<tr>
      <td>${item.resource}</td>
      <td>${item.description}</td>
      <td>${item.cost.toFixed(2)}</td>
      <td>
        <select name="${item.id}" class="category-select">
          <option value="">Select category</option>
          ${categories.map(cat => `<option value="${cat}">${cat}</option>`).join('')}
        </select>
      </td>
      <td class="feedback-cell" id="feedback-${item.id}"></td>
    </tr>`;
  });
  html += '</table>';
  html += '<div class="submit-section"><button type="button" id="submit-categories">Submit Categories</button></div>';
  billSection.innerHTML = html;
  
  // Add event listener for submit button
  document.getElementById('submit-categories').onclick = handleCategorySubmit;
}

function renderCategorizationForm(items) {
  // This function is no longer needed as the form is now integrated into the table
  categorizationSection.innerHTML = '';
  optimizationSection.innerHTML = '';
}

async function handleCategorySubmit(e) {
  e.preventDefault();
  userCategories = {};
  const selects = document.querySelectorAll('.category-select');
  selects.forEach(select => {
    userCategories[select.name] = select.value;
  });
  
  const res = await fetch('/api/validate-categories', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({bill_id: currentBill.bill_id, categories: userCategories})
  });
  const data = await res.json();
  showCategoryResults(data.results);
}

function showCategoryResults(results) {
  let allCorrect = true;
  
  // Clear previous feedback
  document.querySelectorAll('.feedback-cell').forEach(cell => {
    cell.innerHTML = '';
  });
  
  for (let id in results) {
    const r = results[id];
    const feedbackCell = document.getElementById(`feedback-${id}`);
    if (feedbackCell) {
      const status = r.is_correct ? '✅' : '❌';
      const color = r.is_correct ? 'green' : 'red';
      feedbackCell.innerHTML = `<span style="color: ${color}; font-weight: bold;">${status} ${r.correct}</span>`;
    }
    if (!r.is_correct) allCorrect = false;
  }
  
  if (allCorrect) {
    renderOptimizationForm(currentBill.items);
  } else {
    // Add a message below the table
    const submitSection = document.querySelector('.submit-section');
    if (submitSection) {
      submitSection.innerHTML += '<p style="color:red; margin-top: 10px;">Please correct the mistakes and resubmit.</p>';
    }
  }
}

function renderOptimizationForm(items) {
  // Update the step indicator
  const stepHeader = document.querySelector('h3');
  if (stepHeader) {
    stepHeader.textContent = 'Step 2: Choose Best Optimization for Each Item';
  }
  
  // Update the table to include optimization column
  const table = document.querySelector('table');
  if (table) {
    // Update header
    const headerRow = table.querySelector('tr');
    headerRow.innerHTML = '<th>Resource</th><th>Description</th><th>Cost ($)</th><th>Category</th><th>Optimization</th><th>Feedback</th>';
    
    // Update each row to include optimization dropdown
    const rows = table.querySelectorAll('tr:not(:first-child)');
    rows.forEach((row, index) => {
      const item = items[index];
      if (item) {
        const cells = row.querySelectorAll('td');
        if (cells.length >= 5) {
          // Keep first 4 cells (Resource, Description, Cost, Category)
          // Replace 5th cell with optimization dropdown
          cells[4].innerHTML = `
            <select name="${item.id}" class="optimization-select">
              <option value="">Select optimization</option>
              ${optimizations.map(opt => `<option value="${opt}">${opt}</option>`).join('')}
            </select>
          `;
          // Clear feedback cell
          if (cells[5]) {
            cells[5].innerHTML = '';
          }
        }
      }
    });
  }
  
  // Update submit button
  const submitSection = document.querySelector('.submit-section');
  if (submitSection) {
    submitSection.innerHTML = '<button type="button" id="submit-optimizations">Submit Optimizations</button>';
    document.getElementById('submit-optimizations').onclick = handleOptimizationSubmit;
  }
}

async function handleOptimizationSubmit(e) {
  e.preventDefault();
  userOptimizations = {};
  const selects = document.querySelectorAll('.optimization-select');
  selects.forEach(select => {
    userOptimizations[select.name] = select.value;
  });
  
  const res = await fetch('/api/validate-optimizations', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({bill_id: currentBill.bill_id, optimizations: userOptimizations})
  });
  const data = await res.json();
  showOptimizationResults(data);
}

function showOptimizationResults(data) {
  // Display results summary
  let html = `<h3>Results</h3><p>Before: $${data.before_total.toFixed(2)}<br>After: $${data.after_total.toFixed(2)}<br>Savings: <b>$${data.savings.toFixed(2)}</b></p>`;
  
  // Update feedback in the table
  data.details.forEach(item => {
    const feedbackCell = document.getElementById(`feedback-${item.id}`);
    if (feedbackCell) {
      const isCorrect = item.user_opt === item.correct_opt;
      const status = isCorrect ? '✅' : '❌';
      const color = isCorrect ? 'green' : 'red';
      feedbackCell.innerHTML = `<span style="color: ${color}; font-weight: bold;">${status} ${item.correct_opt}</span>`;
    }
  });
  
  // Show detailed results table
  html += '<table><tr><th>Resource</th><th>Your Optimization</th><th>Correct</th><th>Before</th><th>After</th></tr>';
  data.details.forEach(item => {
    html += `<tr><td>${item.resource}</td><td>${item.user_opt}</td><td>${item.correct_opt}</td><td>$${item.cost.toFixed(2)}</td><td>$${item.after_cost.toFixed(2)}</td></tr>`;
  });
  html += '</table>';
  
  resultsSection.innerHTML = html;
  resultsSection.style.display = 'block';
  
  // Hide optimization dropdowns and show restart
  const submitSection = document.querySelector('.submit-section');
  if (submitSection) {
    submitSection.innerHTML = '';
  }
  
  showTip();
  restartBtn.style.display = 'inline-block';
}

async function showTip() {
  const res = await fetch('/api/tips');
  const data = await res.json();
  tipSection.innerHTML = `<b>Tip:</b> ${data.tip}`;
}

restartBtn.onclick = fetchBill;

// Start game on load
fetchBill(); 