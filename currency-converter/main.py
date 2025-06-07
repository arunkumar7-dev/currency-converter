import requests

def get_exchange_rates(base_currency="USD"):
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    try:
        response = requests.get(url)
        data = response.json()
        if data["result"] == "success":
            return data["rates"]
        else:
            print("Error fetching exchange rates:", data.get("error-type", "Unknown error"))
            return None
    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return None

def convert_currency(amount, rate):
    return amount * rate

def main():
    print("Python Currency Converter")

    base_currency = input("Enter the base currency code (e.g., USD): ").upper()
    rates = get_exchange_rates(base_currency)

    if not rates:
        print("Could not get exchange rates. Exiting...")
        return

    target_currency = input("Enter the target currency code (e.g., EUR): ").upper()
    if target_currency not in rates:
        print(f"Currency code '{target_currency}' not found.")
        return

    try:
        amount = float(input(f"Enter amount in {base_currency}: "))
    except ValueError:
        print("Invalid amount entered.")
        return

    rate = rates[target_currency]
    converted_amount = convert_currency(amount, rate)

    print(f"{amount:.2f} {base_currency} = {converted_amount:.2f} {target_currency}")

if __name__ == "__main__":
    main()
