from forex_python.converter import CurrencyRates

# Create an instance of the CurrencyRates class
c = CurrencyRates()

# Function to perform currency conversion
def convert_currency(amount, from_currency, to_currency):
    try:
        # Convert the amount from the source currency to the target currency
        result = c.convert(from_currency, to_currency, amount)
        return result
    except ValueError:
        return "Invalid currency code(s). Please check and try again."

if __name__ == "__main__":
    print("Currency Converter")
    print("Available currencies: USD, EUR, GBP, INR, JPY, AUD, CAD, and more.")

    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the source currency code: ").upper()
    to_currency = input("Enter the target currency code: ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)

    if isinstance(converted_amount, float):
        print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
    else:
        print(converted_amount)
