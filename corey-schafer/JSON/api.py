import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservices/v1/symbols/all/currencies/quotes?format=json") as response:
  source = response.read()

# print(source)

string = json.loads(source)
data = json.dumps(string, indent=2)

print(data)

resources_count = len(string['list']['resources'])
print(resources_count) # 188


amount = ''
base_currency = ''
convert_to = ''
usd_rates = dict()

for item in data['list']['resources']:
  name = item['resource']['fields']['name']
  price = item['resource']['fields']['price']
  usd_rates[name] = price

print(usd_rates['USD/EUR'])
print(50 * float(usd_rates['USD/EUR']))
