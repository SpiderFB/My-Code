import yfinance as yf

# Function to fetch and display stock market data
def fetch_stock_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")  # Fetch data for the last trading day
    
    if not data.empty:
        print(f"Stock Symbol: {symbol}")
        print(data)
    else:
        print(f"No data available for symbol: {symbol}")

# Function to get stock symbols from user
def get_stock_symbols():
    symbols = []
    num_stocks = int(input("Enter the number of stocks: "))
    
    for i in range(num_stocks):
        symbol = input(f"Enter stock symbol {i + 1}: ")
        symbols.append(symbol)
    
    return symbols

# Main program
if __name__ == "__main__":
    print("--- Indian Stock Market Data ---")
    print()
    
    symbols = get_stock_symbols()
    
    for symbol in symbols:
        fetch_stock_data(symbol)
        print()
