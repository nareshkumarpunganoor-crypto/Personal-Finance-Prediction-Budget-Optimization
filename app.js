document.addEventListener('DOMContentLoaded', async () => {
  await checkStatus();
  loadDashboard();
  setupQuickActions();

  document.getElementById('btn-analyze-goal').addEventListener('click', renderSavingsGoal);
});

const checkStatus = async () => {
  const dot = document.getElementById('system-status-dot');
  const text = document.getElementById('system-status-text');
  try {
    const res = await API.getStatus();
    if (res.status === 'online' || res.status === 'ok') {
      dot.classList.add('online');
      text.innerText = 'API Connected';
    } else {
      text.innerText = 'Using Fallback Data';
    }
  } catch (e) {
    text.innerText = 'Using Fallback Data';
  }
};

const loadDashboard = async () => {
  try {
    const [summary, trends, categories, forecast, optimization] = await Promise.all([
      API.getDashboardSummary(),
      API.getTrends(),
      API.getCategories(),
      API.getForecast(),
      API.getOptimization()
    ]);

    // Section 1
    animateCounter(document.getElementById('val-income'), summary.income);
    animateCounter(document.getElementById('val-expenses'), summary.expenses);
    animateCounter(document.getElementById('val-savings'), summary.savings);
    animateCounter(document.getElementById('val-rate'), summary.savingsRate);

    // Section 2 & 3 Charts
    initExpenseForecastChart('expenseForecastChart', trends, forecast);
    initCategoryDonutChart('categoryDonutChart', categories);
    initIncomeExpenseChart('incomeExpenseChart', trends);
    initSavingsProjectionChart('savingsProjectionChart', trends);

    // Section 4 Recommendations
    renderRecommendations(optimization);

  } catch (error) {
    console.error('Failed to load dashboard', error);
    showToast('Failed to load real data. Using fallback.', 'error');
  }
};

const renderRecommendations = (recs) => {
  const container = document.getElementById('recommendations-grid');
  container.innerHTML = '';
  
  recs.forEach(rec => {
    const el = document.createElement('div');
    el.className = 'rec-card';
    el.innerHTML = `
      <div class="rec-header">
        <span class="rec-cat">${rec.category}</span>
        <span class="badge ${rec.priority}">${rec.priority}</span>
      </div>
      <div class="rec-amounts">
        <span>Current: ${formatCurrency(rec.current)}</span>
        <span>Suggested: ${formatCurrency(rec.suggested)}</span>
      </div>
      <div class="rec-savings">Potential Savings: ${formatCurrency(rec.savings)}</div>
      <div class="rec-msg">${rec.message}</div>
    `;
    container.appendChild(el);
  });
};

const renderSavingsGoal = async () => {
  const target = parseFloat(document.getElementById('goal-target').value);
  const timeline = parseFloat(document.getElementById('goal-timeline').value);
  const current = parseFloat(document.getElementById('goal-current').value);

  if (!target || !timeline || isNaN(current)) {
    showToast('Please enter valid goal details', 'error');
    return;
  }

  const btn = document.getElementById('btn-analyze-goal');
  btn.innerText = 'Analyzing...';
  btn.disabled = true;

  try {
    const res = await API.analyzeSavingsGoal(target, timeline, current);
    
    document.getElementById('goal-results').style.display = 'block';
    
    const badge = document.getElementById('goal-feasibility');
    badge.innerText = res.feasible ? 'Achievable' : 'At Risk';
    badge.style.background = res.feasible ? 'rgba(0, 230, 118, 0.2)' : 'rgba(255, 82, 82, 0.2)';
    badge.style.color = res.feasible ? 'var(--income-green)' : 'var(--expense-coral)';

    document.getElementById('goal-monthly').innerText = formatCurrency(res.requiredMonthly);
    document.getElementById('goal-message').innerText = res.message;
    document.getElementById('goal-current-label').innerText = formatCurrency(current);
    document.getElementById('goal-target-label').innerText = formatCurrency(target);

    const progress = Math.min(100, (current / target) * 100);
    setTimeout(() => {
      document.getElementById('goal-progress-fill').style.width = `${progress}%`;
    }, 100);

    showToast('Analysis complete');
  } catch (error) {
    showToast('Failed to analyze goal', 'error');
  } finally {
    btn.innerText = 'Analyze Goal';
    btn.disabled = false;
  }
};

const setupQuickActions = () => {
  const btnGen = document.getElementById('btn-generate');
  const btnTrain = document.getElementById('btn-train');
  const btnRefresh = document.getElementById('btn-refresh');

  btnGen.addEventListener('click', async () => {
    btnGen.innerText = 'Generating...';
    await API.generateData();
    showToast('Synthetic data generated successfully');
    btnGen.innerText = 'Generate Data';
    loadDashboard();
  });

  btnTrain.addEventListener('click', async () => {
    btnTrain.innerText = 'Training...';
    await API.trainModels();
    showToast('AI Models trained successfully');
    btnTrain.innerText = 'Train Models';
    loadDashboard();
  });

  btnRefresh.addEventListener('click', () => {
    loadDashboard();
    checkStatus();
    showToast('Dashboard Refreshed');
  });
};
