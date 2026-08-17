const API = {
  BASE_URL: 'http://localhost:8000/api',

  async get(endpoint, retries = 1) {
    try {
      const response = await fetch(`${this.BASE_URL}${endpoint}`);
      if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
      return await response.json();
    } catch (error) {
      if (retries > 0) {
        console.warn(`Retrying GET ${endpoint}...`);
        return this.get(endpoint, retries - 1);
      }
      console.error(`GET ${endpoint} failed:`, error);
      return this.getFallbackData(endpoint);
    }
  },

  async post(endpoint, data = {}, retries = 1) {
    try {
      const response = await fetch(`${this.BASE_URL}${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
      if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
      return await response.json();
    } catch (error) {
      if (retries > 0) {
        console.warn(`Retrying POST ${endpoint}...`);
        return this.post(endpoint, data, retries - 1);
      }
      console.error(`POST ${endpoint} failed:`, error);
      return this.getFallbackData(endpoint);
    }
  },

  getDashboardSummary() { return this.get('/dashboard/summary'); },
  getTrends() { return this.get('/dashboard/trends'); },
  getCategories() { return this.get('/dashboard/categories'); },
  predictExpenses() { return this.post('/predict/expenses'); },
  getForecast(months = 3) { return this.post('/predict/forecast', { months }); },
  getOptimization() { return this.post('/optimize/budget'); },
  analyzeSavingsGoal(target, timeline, current) {
    return this.post('/optimize/savings-goal', { target, timeline, current });
  },
  getCategoryAnalysis() { return this.get('/optimize/category-analysis'); },
  getStatus() { return this.get('/data/status'); },
  generateData() { return this.post('/data/generate'); },
  trainModels() { return this.post('/data/train'); },

  // Fallback mock data if API is down
  getFallbackData(endpoint) {
    if (endpoint.includes('/dashboard/summary')) {
      return { income: 150000, expenses: 95000, savings: 55000, savingsRate: 36.7 };
    }
    if (endpoint.includes('/dashboard/trends')) {
      return {
        months: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        income: Array(12).fill(150000).map(v => v + (Math.random() * 20000 - 10000)),
        expenses: [80000, 85000, 82000, 90000, 95000, 88000, 92000, 105000, 90000, 95000, 89000, 92000]
      };
    }
    if (endpoint.includes('/dashboard/categories')) {
      return {
        labels: ['Housing', 'Food', 'Transport', 'Entertainment', 'Shopping', 'Utilities'],
        data: [30000, 25000, 15000, 10000, 10000, 5000]
      };
    }
    if (endpoint.includes('/predict/forecast')) {
      return {
        months: ['Jan', 'Feb', 'Mar'],
        predictedExpenses: [93000, 94500, 91000],
        lowerBound: [90000, 90000, 85000],
        upperBound: [96000, 99000, 97000]
      };
    }
    if (endpoint.includes('/optimize/budget')) {
      return [
        { priority: 'high', category: 'Food', current: 25000, suggested: 20000, savings: 5000, message: 'Dining out frequency has increased by 20% this month. Cooking at home could save ₹5,000.' },
        { priority: 'medium', category: 'Entertainment', current: 10000, suggested: 7000, savings: 3000, message: 'You have multiple unused subscriptions. Cancel them to save ₹3,000.' },
        { priority: 'low', category: 'Transport', current: 15000, suggested: 13000, savings: 2000, message: 'Optimizing your commute could save you ₹2,000.' }
      ];
    }
    if (endpoint.includes('/optimize/savings-goal')) {
      return { feasible: true, requiredMonthly: 29166, message: 'Based on current trajectory, you will reach this goal on time.' };
    }
    if (endpoint.includes('/data/status')) {
      return { status: 'offline' };
    }
    return { success: true };
  }
};
