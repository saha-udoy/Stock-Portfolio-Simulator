# data_utils.py
import yfinance as yf
import pandas as pd

def get_data(stocks, start_date="2024-01-01", end_date=None):
    """
    Downloads historical stock data and returns adjusted close prices and daily returns
    
    Args:
        stocks: List of stock tickers
        start_date: Start date for historical data (default: "2024-01-01")
        end_date: End date for historical data (default: None, uses today)
    
    Returns:
        adj_close: DataFrame with adjusted close prices
        returns: DataFrame with daily returns
    """
    if end_date is None:
        from datetime import datetime
        end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Download data for all stocks
    data = yf.download(stocks, start=start_date, end=end_date, group_by='ticker', auto_adjust=True, progress=False)

    adj_close = pd.DataFrame()
    
    # Handle different yfinance data structures
    if len(stocks) == 1:
        # Single ticker returns a simple DataFrame
        if not data.empty and 'Close' in data.columns:
            adj_close[stocks[0]] = data['Close']
    else:
        # Multiple tickers - data should have MultiIndex columns
        if isinstance(data.columns, pd.MultiIndex):
            # MultiIndex columns (group_by='ticker')
            for ticker in stocks:
                if ticker in data.columns.get_level_values(0):
                    try:
                        adj_close[ticker] = data[ticker]['Close']
                    except (KeyError, TypeError):
                        # Try alternative access method
                        try:
                            adj_close[ticker] = data.xs(ticker, level=0, axis=1)['Close']
                        except:
                            continue
        else:
            # Fallback: download each ticker individually
            for ticker in stocks:
                try:
                    ticker_data = yf.download(ticker, start=start_date, end=end_date, 
                                             auto_adjust=True, progress=False)
                    if not ticker_data.empty and 'Close' in ticker_data.columns:
                        adj_close[ticker] = ticker_data['Close']
                except Exception as e:
                    continue

    # Drop any empty columns and align dates
    adj_close = adj_close.dropna(axis=1, how='all')
    
    if adj_close.empty:
        raise ValueError(f"Failed to download data for any of the provided tickers: {stocks}")
    
    # Align all series to common date index
    adj_close = adj_close.dropna()
    
    if adj_close.empty:
        raise ValueError("No overlapping data found for the provided tickers and date range.")
    
    returns = adj_close.pct_change().dropna()
    return adj_close, returns
