#import statements
import requests
import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

#URLs needed
url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
url2 = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

#parameters needed for URL
parameters = {
  'convert':'USD'
}

parameters2 = {
  'start':'1',
  'limit':'1',
  'convert': 'USD'
}

#headers needed for URL
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'Enter your API here',
}

#Session statements
session = Session()
session.headers.update(headers)

#program logic
try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  ls = data['data']
  btc_dominance = ls['btc_dominance']
  eth_dominance = ls['eth_dominance']
  last_updated = ls['last_updated']
  total_market_cap = ls['quote']['USD']['total_market_cap']
  total_volume_24h = ls['quote']['USD']["total_volume_24h"]
  altcoin_volume_24h = ls['quote']['USD']['altcoin_volume_24h']
  altcoin_market_cap = ls['quote']['USD']['altcoin_market_cap']

  response = session.get(url2, params=parameters2)
  data = json.loads(response.text)
  btc_price = data['data'][0]['quote']['USD']['price']
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

#printing fetched information
print("Last Updated     : ", last_updated)
print("BTC price : ", btc_price, " USD")
print()
print("Market Cap")
print("------------------------------------")
print("total_market_cap   : ", total_market_cap, " USD" )
print("btc_market_cap     : ", total_market_cap-altcoin_market_cap, " USD" )
print("altcoin_market_cap : ", altcoin_market_cap, " USD" )
print()
print("Dominance")
print("------------------------------------")
print("btc_dominance    : ", btc_dominance, "%")
print("eth_dominance    : ", eth_dominance, "%")
print()
print("Volume Change")
print("------------------------------------")
print("total_volume_24h   : ", total_volume_24h, " USD")
print("btc_volume_24h     : ", total_volume_24h-altcoin_volume_24h, " USD")
print("altcoin_volume_24h : ", altcoin_volume_24h, " USD")
