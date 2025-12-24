# optimization.py
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def optimize_portfolio(returns, num_portfolios=5000):
    """
    Optimizes portfolio using Efficient Frontier and finds max Sharpe ratio portfolio
    
    Args:
        returns: DataFrame with daily returns
        num_portfolios: Number of random portfolios to generate (default: 5000)
    
    Returns:
        results_df: DataFrame with portfolio results
        max_sharpe: Series with optimal portfolio details
        fig: matplotlib figure object
    """
    stocks = returns.columns
    mean_returns = returns.mean()
    cov_matrix = returns.cov()
    results = []

    for _ in range(num_portfolios):
        weights = np.random.random(len(stocks))
        weights /= np.sum(weights)

        portfolio_return = np.sum(weights * mean_returns) * 252
        portfolio_std = np.sqrt(weights.T @ cov_matrix.values @ weights) * np.sqrt(252)
        sharpe_ratio = portfolio_return / portfolio_std if portfolio_std > 0 else 0

        results.append((portfolio_return, portfolio_std, sharpe_ratio, weights))

    results_df = pd.DataFrame(results, columns=['Return', 'Risk', 'Sharpe', 'Weights'])

    max_sharpe = results_df.iloc[results_df['Sharpe'].idxmax()]
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 7))
    scatter = ax.scatter(results_df['Risk'], results_df['Return'], 
                        c=results_df['Sharpe'], cmap='viridis', 
                        marker='o', s=15, alpha=0.6, edgecolors='none')
    plt.colorbar(scatter, ax=ax, label='Sharpe Ratio')
    
    # Highlight max Sharpe portfolio
    ax.scatter(max_sharpe['Risk'], max_sharpe['Return'], 
              marker='*', color='#FFD700', s=800, 
              edgecolors='black', linewidth=2, 
              label='Max Sharpe Portfolio', zorder=5)
    
    ax.set_xlabel('Risk (Standard Deviation)', fontsize=12)
    ax.set_ylabel('Expected Return (Annualized)', fontsize=12)
    ax.set_title('Efficient Frontier - Portfolio Optimization', fontsize=16, fontweight='bold', pad=20)
    ax.legend(loc='upper left', fontsize=11)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()

    return results_df, max_sharpe, fig
