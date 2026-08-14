Chart.defaults.color = '#9fa8da';
Chart.defaults.font.family = 'Inter';

const darkGrid = 'rgba(255,255,255,0.05)';

let expenseChart, donutChart, incomeExpenseChart, savingsChart;

const initExpenseForecastChart = (canvasId, histData, predData) => {
  const ctx = document.getElementById(canvasId).getContext('2d');
  
  if (expenseChart) expenseChart.destroy();

  const gradientCyan = generateGradient(ctx, 'rgba(0, 210, 255, 0.4)', 'rgba(0, 210, 255, 0.0)');
  const gradientPurple = generateGradient(ctx, 'rgba(123, 47, 247, 0.4)', 'rgba(123, 47, 247, 0.0)');

  expenseChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [...histData.months, ...predData.months],
      datasets: [
        {
          label: 'Historical Expenses',
          data: [...histData.expenses, ...Array(predData.months.length).fill(null)],
          borderColor: '#00d2ff',
          backgroundColor: gradientCyan,
          borderWidth: 3,
          tension: 0.4,
          fill: true,
          pointBackgroundColor: '#0a0e27',
          pointBorderColor: '#00d2ff',
          pointBorderWidth: 2,
          pointRadius: 4,
          pointHoverRadius: 6
        },
        {
          label: 'Predicted Expenses',
          data: [...Array(histData.months.length - 1).fill(null), histData.expenses[histData.expenses.length - 1], ...predData.predictedExpenses],
          borderColor: '#7b2ff7',
          backgroundColor: gradientPurple,
          borderWidth: 3,
          borderDash: [5, 5],
          tension: 0.4,
          fill: true,
          pointBackgroundColor: '#0a0e27',
          pointBorderColor: '#7b2ff7',
          pointBorderWidth: 2,
          pointRadius: 4,
          pointHoverRadius: 6
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      animation: { duration: 1500 },
      plugins: {
        legend: { labels: { color: '#e8eaf6' } },
        tooltip: {
          mode: 'index',
          intersect: false,
          callbacks: {
            label: (ctx) => `${ctx.dataset.label}: ${formatCurrency(ctx.raw)}`
          }
        }
      },
      scales: {
        y: {
          grid: { color: darkGrid },
          ticks: { callback: (val) => formatCurrency(val) }
        },
        x: { grid: { color: darkGrid } }
      }
    }
  });
};

const initCategoryDonutChart = (canvasId, data) => {
  const ctx = document.getElementById(canvasId).getContext('2d');
  
  if (donutChart) donutChart.destroy();

  const total = data.data.reduce((a, b) => a + b, 0);

  const centerTextPlugin = {
    id: 'centerText',
    beforeDraw: (chart) => {
      const { width, height, ctx } = chart;
      ctx.restore();
      const fontSize = (height / 120).toFixed(2);
      ctx.font = `600 ${fontSize}em Inter`;
      ctx.textBaseline = 'middle';
      ctx.fillStyle = '#e8eaf6';
      
      const text = 'Total';
      const textX = Math.round((width - ctx.measureText(text).width) / 2);
      const textY = height / 2 - 15;
      ctx.fillText(text, textX, textY);
      
      ctx.font = `700 ${fontSize * 1.2}em Outfit`;
      const val = formatCurrency(total);
      const valX = Math.round((width - ctx.measureText(val).width) / 2);
      ctx.fillText(val, valX, height / 2 + 15);
      ctx.save();
    }
  };

  donutChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: data.labels,
      datasets: [{
        data: data.data,
        backgroundColor: [
          '#00d2ff', '#7b2ff7', '#00e676', '#ff5252', '#ffc107', '#ff4081'
        ],
        borderWidth: 0,
        hoverOffset: 10
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      cutout: '65%',
      animation: { duration: 1500 },
      plugins: {
        legend: { position: 'bottom', labels: { color: '#e8eaf6', padding: 20 } },
        tooltip: {
          callbacks: {
            label: (ctx) => ` ${ctx.label}: ${formatCurrency(ctx.raw)}`
          }
        }
      }
    },
    plugins: [centerTextPlugin]
  });
};

const initIncomeExpenseChart = (canvasId, data) => {
  const ctx = document.getElementById(canvasId).getContext('2d');
  
  if (incomeExpenseChart) incomeExpenseChart.destroy();

  incomeExpenseChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: data.months.slice(-6),
      datasets: [
        {
          label: 'Income',
          data: data.income.slice(-6),
          backgroundColor: '#00e676',
          borderRadius: 6,
          barPercentage: 0.6,
          categoryPercentage: 0.8
        },
        {
          label: 'Expenses',
          data: data.expenses.slice(-6),
          backgroundColor: '#ff5252',
          borderRadius: 6,
          barPercentage: 0.6,
          categoryPercentage: 0.8
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      animation: { duration: 1500 },
      plugins: {
        legend: { labels: { color: '#e8eaf6' } },
        tooltip: {
          callbacks: { label: (ctx) => `${ctx.dataset.label}: ${formatCurrency(ctx.raw)}` }
        }
      },
      scales: {
        y: { grid: { color: darkGrid }, ticks: { callback: (val) => formatCurrency(val) } },
        x: { grid: { display: false } }
      }
    }
  });
};

const initSavingsProjectionChart = (canvasId, data) => {
  const ctx = document.getElementById(canvasId).getContext('2d');
  
  if (savingsChart) savingsChart.destroy();

  const gradient = generateGradient(ctx, 'rgba(0, 210, 255, 0.6)', 'rgba(0, 210, 255, 0.0)');
  
  let cumulative = 0;
  const savingsData = data.income.map((inc, i) => {
    cumulative += (inc - data.expenses[i]);
    return cumulative;
  });

  savingsChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: data.months,
      datasets: [
        {
          label: 'Cumulative Savings',
          data: savingsData,
          borderColor: '#00d2ff',
          backgroundColor: gradient,
          borderWidth: 3,
          fill: true,
          tension: 0.4,
          pointRadius: 0
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      animation: { duration: 1500 },
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: { label: (ctx) => `Savings: ${formatCurrency(ctx.raw)}` }
        }
      },
      scales: {
        y: { grid: { color: darkGrid }, ticks: { callback: (val) => formatCurrency(val) } },
        x: { grid: { color: darkGrid } }
      }
    }
  });
};
