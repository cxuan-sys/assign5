import yfinance as yf
import streamlit as st

# Define the ticker and risk-free rate
ticker = "MSFT"
rf_monthly = 0.0025  # 0.25% per month

st.title("MSFT Monthly Sharpe Ratio (5 Years)")

# Fetch 5 years of monthly historical data for MSFT
data = yf.Ticker(ticker).history(period="5y", interval="1mo")

if not data.empty:
    close_prices = data["Close"]

    # Calculate monthly returns
    monthly_returns = close_prices.pct_change().dropna()

    # Calculate average excess return and standard deviation of returns
    excess_returns = monthly_returns - rf_monthly
    mean_excess_return = excess_returns.mean()
    std_dev_return = monthly_returns.std()

    # Calculate the Monthly Sharpe Ratio
    monthly_sharpe_ratio = mean_excess_return / std_dev_return

    # Print the results directly to the screen
    st.write(f"Ticker: {ticker}")
    st.metric(label="Monthly Sharpe Ratio", value=f"{monthly_sharpe_ratio:.3f}")
else:
    st.error(f"No data found for {ticker}.")
