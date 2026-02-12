import requests as req
import json
url = "https://api4.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
res = req.get(url).text
print(res[:100])



res = json.loads(res)
a = str(round(float(res["price"])) * 1450) +"원"
b = a[:1]+"억"
c = a[1:5]+"천"
d = a[4:]
print(b+c+d)