import requests

# Function to get supported currencies
def get_supported_currencies(api_key):
    """
    Fetches the list of supported currencies from the Fixer API.

    Args:
    api_key (str): The API key for authenticating with the Fixer API.

    Returns:
    dict: A dictionary of currency codes and names, or None if the API request fails.
    """
    url = f"https://api.apilayer.com/fixer/symbols"
    headers = {
        "apikey": api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('symbols')
    else:
        return None

# Function to get exchange rates
def get_exchange_rate(api_key, base_currency, target_currency, amount):
    """
    Fetches the conversion rate between two currencies using the Fixer API and calculates
    the converted amount.

    Args:
    api_key (str): The API key for authenticating with the Fixer API.
    base_currency (str): The currency to convert from.
    target_currency (str): The currency to convert to.
    amount (float): The amount of base_currency to convert.

    Returns:
    float: The converted amount in the target currency, or None if the API request fails.
    """
    url = (
        f"https://api.apilayer.com/fixer/convert"
        f"?to={target_currency}"
        f"&from={base_currency}"
        f"&amount={amount}"
    )
    headers = {
        "apikey": api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('result')
    else:
        return None

def main():
    """
    Main function to handle user input, fetch exchange rates, and display the conversion result.
    """
    # Replace with your actual API key from the Fixer API
    api_key = "XeBVyNXAQx4aPeRjZVJawG13EKSfbHEE"

    # Fetch supported currencies
    currencies = get_supported_currencies(api_key)
    if not currencies:
        print("Unable to fetch the list of supported currencies. Please check your API key and try again.")
        return

    # Display available currencies
    print("Available currencies:")
    for code, name in currencies.items():
        print(f"{code}: {name}")

    while True:
        # Get user input for the base currency
        base_currency = input("Enter the initial currency code (e.g., USD): ").upper()
        if base_currency not in currencies:
            print("Invalid currency code. Please choose from the available currencies.")
            continue

        # Get user input for the target currency
        target_currency = input("Enter the target currency code (e.g., EUR): ").upper()
        if target_currency not in currencies:
            print("Invalid currency code. Please choose from the available currencies.")
            continue
        
        try:
            # Get user input for the amount to convert
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                print("Please enter an amount greater than 0.")
                continue
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue

        # Fetch the converted amount using the API
        converted_amount = get_exchange_rate(api_key, base_currency, target_currency, amount)
        if converted_amount is not None:
            # Print the conversion result
            print(f"{amount} {currencies[base_currency]} ({base_currency}) is equal to {converted_amount:.2f} {currencies[target_currency]} ({target_currency})")
        else:
            print("There is an issue with the response from the API.")

        # Ask the user if they want to perform another conversion
        try_again = input("Do you want to try again? (yes/no): ").strip().lower()
        if try_again != 'yes':
            break

    print("Exiting the program.")

if __name__ == "__main__":
    main()
