import pandas as pd

# Load data
df = pd.read_csv('data.csv')
df['MA_fast'] = df['Close'].rolling(window=10).mean()
df['MA_slow'] = df['Close'].rolling(window=30).mean()

# Generate signals
df['Signal'] = 0
df.loc[df['MA_fast'] > df['MA_slow'], 'Signal'] = 1
df.loc[df['MA_fast'] < df['MA_slow'], 'Signal'] = -1
df['Position'] = df['Signal'].shift(1)

# Calculate returns
df['Market Return'] = df['Close'].pct_change()
df['Strategy Return'] = df['Position'] * df['Market Return']
df['Equity Curve'] = (1 + df['Strategy Return']).cumprod()

# Show final results
print("Total Return: {:.2f}%".format((df['Equity Curve'].iloc[-1] - 1) * 100))
