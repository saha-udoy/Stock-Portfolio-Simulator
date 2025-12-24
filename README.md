# Stock Portfolio Simulator 📈

An advanced, interactive web application for stock portfolio analysis, backtesting, Monte Carlo simulation, and optimization using the Efficient Frontier approach.

## Features

- 📊 **Historical Backtesting**: Analyze how your portfolio would have performed using historical data
- 🎲 **Monte Carlo Simulation**: Predict future portfolio values with confidence intervals
- ⚡ **Portfolio Optimization**: Find the optimal allocation using Efficient Frontier analysis
- 📈 **Interactive Visualizations**: Three dynamic charts showing portfolio growth, Monte Carlo results, and Efficient Frontier
- 🎨 **Modern Web Interface**: Beautiful, user-friendly Streamlit interface

## Installation

1. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Activate your virtual environment** (if not already activated):
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

3. **Open your browser** to the URL shown in the terminal (usually `http://localhost:8501`)

4. **Configure your portfolio**:
   - Enter 3 stock tickers (e.g., AAPL, MSFT, GOOGL)
   - Set investment amounts for each stock
   - Adjust date range and Monte Carlo parameters (optional)
   - Click "Run Analysis"

## Project Structure

```
Stock Simulator/
├── app.py                 # Streamlit web application
├── data_utils.py          # Data downloading and processing
├── backtest.py            # Portfolio backtesting module
├── monte_carlo.py         # Monte Carlo simulation module
├── optimization.py        # Efficient Frontier optimization
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Requirements

- Python 3.8+
- Internet connection (for downloading stock data)
- All dependencies listed in `requirements.txt`

## How It Works

1. **Data Download**: Fetches historical stock data using yfinance
2. **Backtesting**: Calculates portfolio value over time using historical returns
3. **Monte Carlo**: Simulates thousands of possible future scenarios
4. **Optimization**: Generates random portfolios and finds the one with maximum Sharpe ratio

## Example

Try these default settings:
- **Stocks**: AAPL, MSFT, GOOGL
- **Investments**: $1,000 each
- **Date Range**: Last 2 years

## Notes

- Stock data is fetched in real-time from Yahoo Finance
- Monte Carlo simulations may take a few seconds depending on the number of simulations
- Results are based on historical data and should not be considered as financial advice

