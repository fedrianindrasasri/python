import json
from urllib import request

url = "https://indonesia-covid-19.mathdro.id/api/provinsi"

response = request.urlopen(url)

data = json.loads(response.read())

for covid in data['data']:
    print(f"- {covid['provinsi']} : ")
    print(f" Positif: {covid['kasusPosi']} ")
    print(f" Sembuh: {covid['kasusSemb']} ")
    print(f" Meninggal: {covid['kasusMeni']} ")