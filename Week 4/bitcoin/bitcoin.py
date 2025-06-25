import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Argument must be a number.")

    try:
        response = requests.get("https://api.coincap.io/v3/assets/bitcoin?apiKey=1898ee4f36265d3015686f6a2455a523e3b8d534e11a289ae74798294c6b4ff9")
        response.raise_for_status()
        data = response.json()
        price_usd = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error: Failed to fetch Bitcoin price.")
    except (KeyError, TypeError, ValueError):
        sys.exit("Error: Unexpected API response format.")

    total_cost = bitcoins * price_usd

    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
