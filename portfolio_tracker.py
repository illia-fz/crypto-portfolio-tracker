import requests


def fetch_price(symbol):
    """Fetch the current USD price for a cryptocurrency from CoinGecko"""
    try:
        response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd")
        data = response.json()
        return data[symbol]['usd']
    except Exception as e:
        print("Error fetching price:", e)
        return None


def main():
    # Define your cryptocurrency portfolio: symbol -> amount held
    portfolio = {
        "bitcoin": 0.1,
        "ethereum": 1.5,
        "litecoin": 10
    }
    total_value = 0.0
    for symbol, amount in portfolio.items():
        price = fetch_price(symbol)
   

def rebalance_portfolio(portfolio, target_allocations):
    """Rebalance the portfolio to match the target allocations."""
    total_value = 0.0
    prices = {}
    # Calculate current total value and store prices
    for symbol, amount in portfolio.items():
        price = fetch_price(symbol)
        if price:
            prices[symbol] = price
            total_value += amount * price
    # Determine desired trades to reach target allocations
    for symbol, target_percent in target_allocations.items():
        desired_value = total_value * target_percent
        current_value = portfolio.get(symbol, 0) * prices.get(symbol, 0)
        diff_value = desired_value - current_value
        if abs(diff_value) > 0:
            action = 'buy' if diff_value > 0 else 'sell'
            print(f"To rebalance, you should {action} ${abs(diff_value):.2f} worth of {symbol}.")


    
# Update main to include rebalancing example

def main():
    # Define your cryptocurrency portfolio: symbol -> amount held
    portfolio = {
        "bitcoin": 0.1,
        "ethereum": 1.5,
        "litecoin": 10
    }
    total_value = 0.0
    for symbol, amount in portfolio.items():
        price = fetch_price(symbol)
        if price:
            value = price * amount
            total_value += value
            print(f"{symbol}: {amount} x ${price:.2f} = ${value:.2f}")
    print(f"Total portfolio value: ${total_value:.2f}")

    # Example target allocations for rebalancing (50% BTC, 30% ETH, 20% LTC)
    target_allocations = {
        "bitcoin": 0.5,
        "ethereum": 0.3,
        "litecoin": 0.2
    }
    rebalance_portfolio(portfolio, target_allocations)


if __name__ == "__main__":
    main()
     if price:
            value = price * amount
            total_value += value
            print(f"{symbol}: {amount} x ${price:.2f} = ${value:.2f}")
    print(f"Total portfolio value: ${total_value:.2f}")


if __name__ == "__main__":
    main()
