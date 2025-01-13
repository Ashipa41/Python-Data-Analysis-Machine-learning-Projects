#                                                    Apple Stock Market Analysis and insights
# Objective
The purpose of this analysis was to explore the behavior of Apple Inc.'s stock prices from 2020 to 2024, using various financial metrics and visualizations to gain insights into price trends, returns, volatility, and trading signal.

# About Dataset
This Dataset Contains 1238 rows and 7 columns. The data span from (2020 - 2024).
1. This data is collected from Yahoo Finance
2. This data is collected from 2020-01-01 to 2024-12-01
3. This data is collected from Apple Inc.

# This data have following features:
1. Open: The opening price of the stock on a given day.
2. High: The highest price of the stock on a given day.
3. Low: The lowest price of the stock on a given day.
4. Close: The closing price of the stock on a given day.
5. Volume: The total number of shares traded on a given day.
6. Adj Close: The adjusted closing price of the stock on a given day.

# Exploratory Data Analysis (EDA):
- Checking for missing values.
- Summary statistics.
- Visualization of trends.



2. Moving Averages (30-Day and 100-Day)
The moving averages provide a smoothed view of the price trend:
- The 30-day moving average reacts to short-term price changes more quickly.

- Long-term trends can be seen more broadly with the help of the 100-day moving average.
  Generally speaking, a bullish trend is indicated when the 30-day MA crosses above the 100-day MA, while a negative trend is indicated when it crosses below.

3. Daily Volatility
Volatility was measured as the 30-day rolling standard deviation of daily returns:
- Periods of increased volatility align with sharp price movements, often during market uncertainty.
- Volatility generally remains within manageable levels, reflecting the relative stability of AAPL as a blue-chip stock. 

4. Close Price vs. Volume
The scatter plot between closing price and trading volume revealed:
- Higher volumes often coincide with significant price movements, either upward or downward.
- The relationship suggests that periods of high trading activity often follow news or major events.

5.  Daily resturns
Daily returns shows significant fluctuations, with occasional spikes. For short-term traders, this volatility draws attention to both the risk and the opportunity. A mean-reverting pattern is observed, suggesting frequent oscillations around zero daily return.

# Conclusion

The analysis of AAPL stock data highlights its strong performance as a long-term investment due to consistent cumulative returns and robust price trends. Short-term trading opportunities exist through tactical strategies like SMA crossovers and volume analysis. AAPL demonstrates resilience and stability, making it suitable for both risk-averse investors and active traders. By monitoring volatility and leveraging insights from trading volume, investors can align their strategies with market conditions effectively.
