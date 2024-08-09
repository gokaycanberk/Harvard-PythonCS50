import requests
import sys

if len(sys.argv) ==2:
    try:
        value = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)



try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response.raise_for_status()
    data = response.json()
    btcPrice = data['bpi']['USD']['rate_float']
    amount = btcPrice * value
    print(f"${amount:,.4f}")
except requests.RequestException:
    print("RequestException")
    sys.exit(1)
