# monte_carlo.py
import numpy as np
import matplotlib.pyplot as plt

def run_monte_carlo(adj_close, returns, investments, simulations=1000, days=252):
    """
    Runs Monte Carlo simulation to predict future portfolio values
    
    Args:
        adj_close: DataFrame with adjusted close prices
        returns: DataFrame with daily returns
        investments: Dictionary mapping stock tickers to investment amounts
        simulations: Number of Monte Carlo simulations (default: 1000)
        days: Number of trading days to simulate (default: 252, ~1 year)
    
    Returns:
        portfolio_end_values: Array of simulated portfolio end values
        stats: Dictionary with statistics (expected, 5th percentile, 95th percentile)
        fig: matplotlib figure object
    """
    stocks = adj_close.columns
    initial_prices = adj_close.iloc[-1].values
    total_investment = sum(investments.values())
    
    # Calculate initial shares for each stock (handle division by zero)
    initial_shares = []
    for i, stock in enumerate(stocks):
        investment = investments.get(stock, 0)
        price = initial_prices[i]
        if price > 0:
            initial_shares.append(investment / price)
        else:
            initial_shares.append(0)
    initial_shares = np.array(initial_shares)
    
    portfolio_end_values = []

    for _ in range(simulations):
        simulated_prices = initial_prices.copy()
        for _ in range(days):
            daily_returns = returns.sample(n=1, replace=True).values.flatten()
            simulated_prices = simulated_prices * (1 + daily_returns)
        portfolio_value = np.sum(simulated_prices * initial_shares)
        portfolio_end_values.append(portfolio_value)

    portfolio_end_values = np.array(portfolio_end_values)
    
    # Calculate statistics
    stats = {
        'expected': portfolio_end_values.mean(),
        'percentile_5': np.percentile(portfolio_end_values, 5),
        'percentile_95': np.percentile(portfolio_end_values, 95),
        'median': np.median(portfolio_end_values)
    }

    # Create figure
    fig, ax = plt.subplots(figsize=(12, 6))
    n, bins, patches = ax.hist(portfolio_end_values, bins=50, color='#A23B72', 
                               edgecolor='white', linewidth=1.2, alpha=0.8)
    
    # Color code bins
    for i, patch in enumerate(patches):
        if bins[i] <= stats['percentile_5']:
            patch.set_facecolor('#E63946')  # Red for worst case
        elif bins[i] >= stats['percentile_95']:
            patch.set_facecolor('#06A77D')  # Green for best case
        else:
            patch.set_facecolor('#A23B72')  # Purple for normal
    
    # Add vertical lines for statistics
    ax.axvline(stats['expected'], color='#F77F00', linestyle='--', linewidth=2, 
               label=f"Expected: ${stats['expected']:,.2f}")
    ax.axvline(stats['percentile_5'], color='#E63946', linestyle='--', linewidth=2, 
               label=f"5th Percentile: ${stats['percentile_5']:,.2f}")
    ax.axvline(stats['percentile_95'], color='#06A77D', linestyle='--', linewidth=2, 
               label=f"95th Percentile: ${stats['percentile_95']:,.2f}")
    
    ax.set_title("Monte Carlo Simulation of Portfolio Value", fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel("Portfolio Value ($)", fontsize=12)
    ax.set_ylabel("Frequency", fontsize=12)
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(True, alpha=0.3, linestyle='--', axis='y')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()

    return portfolio_end_values, stats, fig
