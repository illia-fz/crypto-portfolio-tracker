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
        if price:
            value = price * amount
            total_value += value
            print(f"{symbol}: {amount} x ${price:.2f} = ${value:.2f}")
    print(f"Total portfolio value: ${total_value:.2f}")


if __name__ == "__main__":
    main()
