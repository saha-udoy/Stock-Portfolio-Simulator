# app.py - Streamlit Web Application
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Import backend modules
from data_utils import get_data
from backtest import backtest_portfolio
from monte_carlo import run_monte_carlo
from optimization import optimize_portfolio

# Page configuration
st.set_page_config(
    page_title="Stock Portfolio Simulator",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(90deg, #2E86AB 0%, #A23B72 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #2E86AB;
    }
    .stButton>button {
        width: 100%;
        background-color: #2E86AB;
        color: white;
        font-weight: 600;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #1e5f7a;
    }
    </style>
""", unsafe_allow_html=True)

def render_header():
    """Render the main header with title and author"""
    st.markdown('<h1 class="main-header">Stock Portfolio Simulator</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #666; font-size: 1.1rem; margin-top: -1rem; margin-bottom: 2rem;">By Udoy Saha</p>', unsafe_allow_html=True)
    st.markdown("---")

def about_page():
    """About page content"""
    render_header()
    
    st.markdown("""
    ## About This Project
    
    The Stock Portfolio Simulator is an advanced web application designed to help investors 
    analyze and optimize their stock portfolios through comprehensive financial modeling and 
    simulation techniques.
    
    ### Features
    
    **Historical Backtesting**
    
    Analyze how your portfolio would have performed using historical stock data. The backtesting 
    module calculates portfolio value over time based on your specified investment amounts and 
    actual historical returns, providing insights into past performance.
    
    **Monte Carlo Simulation**
    
    Predict future portfolio values using Monte Carlo methods. This simulation runs thousands 
    of scenarios based on historical return distributions to provide:
    - Expected portfolio value
    - 5th percentile (worst-case scenario)
    - 95th percentile (best-case scenario)
    
    The results are visualized in a histogram that shows the distribution of possible outcomes, 
    helping you understand the range of potential portfolio values.
    
    **Portfolio Optimization**
    
    Discover the optimal portfolio allocation using Modern Portfolio Theory and the Efficient 
    Frontier approach. The optimization algorithm:
    - Generates thousands of random portfolio combinations
    - Calculates risk, return, and Sharpe ratio for each
    - Identifies the portfolio with maximum Sharpe ratio (best risk-adjusted return)
    
    The Efficient Frontier visualization shows all possible portfolios, with the optimal 
    portfolio highlighted, allowing you to compare your current allocation against the 
    mathematically optimal one.
    
    ### Technical Implementation
    
    This application is built using:
    - **Streamlit** for the interactive web interface
    - **yfinance** for real-time stock data retrieval
    - **Pandas** and **NumPy** for data processing and calculations
    - **Matplotlib** for data visualization
    - Modern Portfolio Theory for optimization algorithms
    
    ### How It Works
    
    1. **Data Collection**: Historical stock data is downloaded from Yahoo Finance for the 
       specified date range
    2. **Backtesting**: Portfolio value is calculated day-by-day using historical returns 
       and your investment weights
    3. **Monte Carlo**: Random sampling of historical returns is used to simulate thousands 
       of possible future scenarios
    4. **Optimization**: Random portfolio weights are generated and evaluated to find the 
       optimal risk-return trade-off
    
    ### Use Cases
    
    - **Portfolio Analysis**: Understand how your current portfolio allocation performs
    - **Investment Planning**: Explore different investment scenarios before committing capital
    - **Risk Assessment**: Identify potential downside and upside scenarios
    - **Allocation Optimization**: Discover mathematically optimal portfolio weights
    
    ### Important Notes
    
    - Results are based on historical data and should not be considered as financial advice
    - Past performance does not guarantee future results
    - The simulations assume that historical patterns will continue, which may not always be the case
    - Always consult with a financial advisor before making investment decisions
    
    ### Getting Started
    
    Navigate to the main page using the sidebar to begin analyzing your portfolio. Enter three 
    stock tickers, specify your investment amounts, and click "Run Analysis" to see comprehensive 
    results including historical performance, future projections, and optimization recommendations.
    """)

def main():
    # Navigation
    page = st.sidebar.selectbox("Navigation", ["Portfolio Analysis", "About"])
    
    if page == "About":
        about_page()
        return
    
    # Main analysis page
    render_header()
    
    # Sidebar for user inputs
    with st.sidebar:
        st.header("Portfolio Configuration")
        st.markdown("---")
        
        # Stock ticker inputs
        st.subheader("Stock Tickers")
        ticker1 = st.text_input("Stock 1", value="AAPL", placeholder="e.g., AAPL", key="ticker1")
        ticker2 = st.text_input("Stock 2", value="MSFT", placeholder="e.g., MSFT", key="ticker2")
        ticker3 = st.text_input("Stock 3", value="GOOGL", placeholder="e.g., GOOGL", key="ticker3")
        
        st.markdown("---")
        
        # Investment amounts
        st.subheader("Investment Amounts ($)")
        invest1 = st.number_input(f"Investment for {ticker1.upper()}", 
                                  min_value=0.0, value=1000.0, step=100.0, key="invest1")
        invest2 = st.number_input(f"Investment for {ticker2.upper()}", 
                                  min_value=0.0, value=1000.0, step=100.0, key="invest2")
        invest3 = st.number_input(f"Investment for {ticker3.upper()}", 
                                  min_value=0.0, value=1000.0, step=100.0, key="invest3")
        
        st.markdown("---")
        
        # Date range selection
        st.subheader("Date Range")
        default_start = datetime.now() - timedelta(days=365*2)  # 2 years back
        start_date = st.date_input("Start Date", value=default_start, key="start_date")
        end_date = st.date_input("End Date", value=datetime.now(), key="end_date")
        
        st.markdown("---")
        
        # Monte Carlo parameters
        st.subheader("Monte Carlo Settings")
        num_simulations = st.slider("Number of Simulations", 500, 5000, 1000, step=500, key="simulations")
        simulation_days = st.slider("Simulation Period (days)", 30, 504, 252, step=30, key="days")
        
        st.markdown("---")
        
        # Run analysis button
        run_analysis = st.button("Run Analysis", type="primary", use_container_width=True)
        
        # Info section
        st.markdown("---")
        st.info("**Tip:** Enter valid stock tickers and investment amounts, then click 'Run Analysis' to see your portfolio performance!")
    
    # Main content area
    if run_analysis:
        # Validate inputs
        stocks = [ticker1.upper().strip(), ticker2.upper().strip(), ticker3.upper().strip()]
        investments = {
            stocks[0]: invest1,
            stocks[1]: invest2,
            stocks[2]: invest3
        }
        
        # Check if all tickers are provided
        if not all(stocks) or any(len(s) == 0 for s in stocks):
            st.error("Please enter all three stock tickers!")
            return
        
        # Check if investments sum to more than 0
        total_investment = sum(investments.values())
        if total_investment == 0:
            st.error("Please enter investment amounts greater than 0!")
            return
        
        # Show loading spinner
        with st.spinner("Fetching data and running analysis... This may take a moment."):
            try:
                # 1. Download data
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                status_text.text("Downloading historical stock data...")
                progress_bar.progress(10)
                
                adj_close, returns = get_data(stocks, start_date=str(start_date), end_date=str(end_date))
                
                if adj_close.empty or returns.empty:
                    st.error("Failed to download data. Please check your ticker symbols and try again.")
                    return
                
                progress_bar.progress(30)
                status_text.text("Running backtest analysis...")
                
                # 2. Backtest
                portfolio_value, backtest_fig = backtest_portfolio(returns, investments)
                
                progress_bar.progress(50)
                status_text.text("Running Monte Carlo simulation...")
                
                # 3. Monte Carlo
                mc_values, mc_stats, mc_fig = run_monte_carlo(
                    adj_close, returns, investments, 
                    simulations=num_simulations, days=simulation_days
                )
                
                progress_bar.progress(75)
                status_text.text("Optimizing portfolio (Efficient Frontier)...")
                
                # 4. Optimization
                opt_results, max_sharpe, opt_fig = optimize_portfolio(returns)
                
                progress_bar.progress(100)
                status_text.text("Analysis complete!")
                
                # Clear progress indicators
                progress_bar.empty()
                status_text.empty()
                
                # Display results
                st.success("Analysis completed successfully!")
                
                # Summary metrics
                st.markdown("## Portfolio Summary")
                col1, col2, col3, col4 = st.columns(4)
                
                final_value = portfolio_value.iloc[-1]
                total_return = ((final_value - total_investment) / total_investment) * 100
                
                with col1:
                    st.metric("Total Investment", f"${total_investment:,.2f}")
                with col2:
                    st.metric("Current Portfolio Value", f"${final_value:,.2f}")
                with col3:
                    st.metric("Total Return", f"{total_return:.2f}%", 
                             delta=f"${final_value - total_investment:,.2f}")
                with col4:
                    st.metric("Expected Future Value (MC)", f"${mc_stats['expected']:,.2f}")
                
                st.markdown("---")
                
                # Portfolio allocation
                st.markdown("## Portfolio Allocation")
                allocation_df = pd.DataFrame({
                    'Stock': stocks,
                    'Investment': [investments[s] for s in stocks],
                    'Weight': [f"{(investments[s]/total_investment)*100:.1f}%" for s in stocks]
                })
                st.dataframe(allocation_df, use_container_width=True, hide_index=True)
                
                st.markdown("---")
                
                # Visualizations
                st.markdown("## Visualizations")
                
                # Portfolio Growth Chart
                st.markdown("### 1. Portfolio Growth Over Time")
                st.pyplot(backtest_fig, use_container_width=True)
                
                # Monte Carlo Results
                st.markdown("### 2. Monte Carlo Simulation Results")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Expected Value", f"${mc_stats['expected']:,.2f}")
                with col2:
                    st.metric("5th Percentile (Worst Case)", f"${mc_stats['percentile_5']:,.2f}", 
                             delta=f"${mc_stats['percentile_5'] - total_investment:,.2f}")
                with col3:
                    st.metric("95th Percentile (Best Case)", f"${mc_stats['percentile_95']:,.2f}", 
                             delta=f"${mc_stats['percentile_95'] - total_investment:,.2f}")
                
                st.pyplot(mc_fig, use_container_width=True)
                
                # Efficient Frontier
                st.markdown("### 3. Efficient Frontier - Portfolio Optimization")
                
                # Display optimal portfolio details
                st.markdown("#### Optimal Portfolio (Max Sharpe Ratio)")
                opt_col1, opt_col2, opt_col3 = st.columns(3)
                
                with opt_col1:
                    st.metric("Expected Return", f"{max_sharpe['Return']*100:.2f}%")
                with opt_col2:
                    st.metric("Risk (Std Dev)", f"{max_sharpe['Risk']*100:.2f}%")
                with opt_col3:
                    st.metric("Sharpe Ratio", f"{max_sharpe['Sharpe']:.3f}")
                
                # Optimal weights
                st.markdown("**Optimal Weights:**")
                optimal_weights = pd.DataFrame({
                    'Stock': stocks,
                    'Optimal Weight': [f"{w*100:.2f}%" for w in max_sharpe['Weights']],
                    'Current Weight': [f"{(investments[s]/total_investment)*100:.2f}%" for s in stocks]
                })
                st.dataframe(optimal_weights, use_container_width=True, hide_index=True)
                
                st.pyplot(opt_fig, use_container_width=True)
                
                # Additional insights
                st.markdown("---")
                st.markdown("## Insights")
                
                # Compare current vs optimal
                current_weights = np.array([investments[s]/total_investment for s in stocks])
                optimal_weights_array = max_sharpe['Weights']
                
                # Calculate current portfolio metrics
                mean_returns = returns.mean()
                cov_matrix = returns.cov()
                current_return = np.sum(current_weights * mean_returns) * 252
                current_risk = np.sqrt(current_weights.T @ cov_matrix.values @ current_weights) * np.sqrt(252)
                current_sharpe = current_return / current_risk if current_risk > 0 else 0
                
                insight_col1, insight_col2 = st.columns(2)
                
                with insight_col1:
                    st.info(f"""
                    **Current Portfolio Performance:**
                    - Return: {current_return*100:.2f}%
                    - Risk: {current_risk*100:.2f}%
                    - Sharpe Ratio: {current_sharpe:.3f}
                    """)
                
                with insight_col2:
                    improvement = ((max_sharpe['Sharpe'] - current_sharpe) / current_sharpe * 100) if current_sharpe > 0 else 0
                    st.success(f"""
                    **Optimal Portfolio Performance:**
                    - Return: {max_sharpe['Return']*100:.2f}%
                    - Risk: {max_sharpe['Risk']*100:.2f}%
                    - Sharpe Ratio: {max_sharpe['Sharpe']:.3f}
                    - Improvement: {improvement:.1f}%
                    """)
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.info("Please check that:")
                st.info("1. All stock tickers are valid")
                st.info("2. The date range is valid")
                st.info("3. You have an internet connection")
    
    else:
        # Welcome screen
        st.markdown("""
        ## Welcome to the Stock Portfolio Simulator
        
        This interactive tool allows you to:
        
        - **Backtest** your portfolio performance using historical data
        - **Simulate** future portfolio values using Monte Carlo methods
        - **Optimize** your portfolio using the Efficient Frontier approach
        
        ### Getting Started
        
        1. **Enter Stock Tickers**: Input 3 stock ticker symbols (e.g., AAPL, MSFT, GOOGL)
        2. **Set Investment Amounts**: Specify how much you want to invest in each stock
        3. **Configure Settings**: Adjust date range and Monte Carlo parameters (optional)
        4. **Run Analysis**: Click the "Run Analysis" button to see your results!
        
        ### Features
        
        - **Portfolio Growth Chart**: See how your portfolio would have performed historically
        - **Monte Carlo Histogram**: Visualize potential future portfolio values with confidence intervals
        - **Efficient Frontier**: Discover the optimal portfolio allocation for maximum risk-adjusted returns
        
        ---
        
        **Ready to get started?** Use the sidebar to configure your portfolio and click "Run Analysis"!
        """)
        
        # Example portfolio
        st.markdown("### Example Configuration")
        example_col1, example_col2 = st.columns(2)
        
        with example_col1:
            st.markdown("""
            **Stocks:**
            - AAPL (Apple)
            - MSFT (Microsoft)
            - GOOGL (Google)
            
            **Investments:**
            - $1,000 per stock
            - Total: $3,000
            """)
        
        with example_col2:
            st.markdown("""
            **What you'll see:**
            - Historical performance
            - Future value predictions
            - Optimal allocation recommendations
            """)

if __name__ == "__main__":
    main()

