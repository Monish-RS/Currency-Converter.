exchange_rates = {
     'USD': 1.0,
     'EUR': 0.91,
     'GBP': 0.78,
     'INR': 82.31,
     'AUD': 1.51,
     'SGD': 1.41,
 }
def get_user_input():
     amount = float(input("Enter the amount: "))
     from_currency = input("Enter the currency we want to convert from (USD, EUR, GBP,INR,AUD,SGD): ").upper()
     to_currency = input("Enter the currency we want to convert to (USD, EUR, GBP,INR,AUD,SGD): ").upper()

     return amount, from_currency, to_currency
def convert_currency(amount, from_currency, to_currency):
     if from_currency == to_currency:
         return amount

     if from_currency not in exchange_rates or to_currency not in exchange_rates:
         raise ValueError("Invalid currency provided.")

     return amount * exchange_rates[to_currency] / exchange_rates[from_currency]
def main():
     try:
         amount, from_currency, to_currency = get_user_input()
         result = convert_currency(amount, from_currency, to_currency)
         print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
     except ValueError as e:
         print(e)

if __name__ == "__main__":
     main()
