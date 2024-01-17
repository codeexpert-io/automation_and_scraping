#BITCOIN PRICE INDEX
import sys
import json
import requests

#gets valid arguments
try:
    bit=float(sys.argv[1])
except ValueError:
    sys.exit("invalid usage")
except IndexError:
    sys.exit("missing argument")

#scrapes bitcoin price data and converts to dollars
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
o=response.json()
conversion=o["bpi"]["USD"]["rate_float"]
current=conversion*bit
print(f"${current:,.4f}")

