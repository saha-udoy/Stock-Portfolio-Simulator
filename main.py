# main.py
from data_utils import get_data
from backtest import backtest_portfolio
from monte_carlo import run_monte_carlo
from optimization import optimize_portfolio

stocks = ['AAPL', 'MSFT', 'GOOGL']

# 1. Download data
adj_close, returns = get_data(stocks)

# 2. Backtest historical portfolio
portfolio_backtest = backtest_portfolio(returns)

# 3. Run Monte Carlo simulation
monte_carlo_results = run_monte_carlo(adj_close, returns)

# 4. Portfolio Optimization
optimization_results, max_sharpe = optimize_portfolio(returns)
