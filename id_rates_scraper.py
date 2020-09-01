import requests

json_data1 = requests.get("http://www.floatrates.com/daily/idr.json")

print(json_data1.json())
print(json_data1.text)

json_data2 = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.8897023414369e-5,"date":"Tue, 1 Sep 2020 00:00:01 GMT","inverseRate":14514.41514368}}

for i in json_data2.values():
    print('Code:',i['code'])
    print('Name:',i['name'])
    print('Date:',i['date'])
    print('Inverse Rate:',i['inverseRate'])