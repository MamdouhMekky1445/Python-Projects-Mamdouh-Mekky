import requests

base_currency = input("Enter the initial currency (e.g., USD): ").upper()
target_currency = input("Enter the target currency (e.g., EUR): ").upper()
        
while True:
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        continue
    
    if amount <= 0:
        print("Please enter an amount greater than 0.")
        continue
    else:
        break
   
url = (
    f"https://api.apilayer.com/fixer/convert?to={target_currency}"
    f"&from={base_currency}"
    f"&amount={amount}"
)

payload = {}
headers= {
  "apikey": "XeBVyNXAQx4aPeRjZVJawG13EKSfbHEE"
}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code

if status_code != 200:
    print("There is an issue with the response. Please try again later.")
    exit()

obj_result = response.json()
final_result = obj_result.get('result')

if final_result is not None:
    print(f"{amount} in {base_currency} = {final_result} in {target_currency}")
else:
    print("There is an issue with the conversion result. Please try again later.")
