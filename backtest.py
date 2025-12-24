# backtest.py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def backtest_portfolio(returns, investments):
    """
    Backtests portfolio with custom investment amounts per stock
    
    Args:
        returns: DataFrame with daily returns
        investments: Dictionary mapping stock tickers to investment amounts
    
    Returns:
        portfolio_value: Series with portfolio value over time
        fig: matplotlib figure object
    """
    stocks = returns.columns
    total_investment = sum(investments.values())
    
    # Calculate weights based on investment amounts
    weights = np.array([investments.get(stock, 0) for stock in stocks])
    weights = weights / weights.sum() if weights.sum() > 0 else np.repeat(1 / len(stocks), len(stocks))
    
    cumulative_returns = (1 + returns).cumprod()
    portfolio_value = (cumulative_returns @ weights) * total_investment
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(portfolio_value.index, portfolio_value.values, linewidth=2, color='#2E86AB')
    ax.set_title("Portfolio Growth Over Time", fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Portfolio Value ($)", fontsize=12)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    
    return portfolio_value, fig
