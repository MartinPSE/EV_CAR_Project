# 기상청 skt developement api
import os
import json
import requests

lat_lon = {
	"Chunchun":["37.9026","127.7357"]
}

location = "Chunchun"
appKey = "99471af8-5abb-451b-9b99-c18a340acd23"
params = {"version": "1", "lat": lat_lon[location][0], "lon": lat_lon[location][1]}
# your_api_key에 발급받은 api key를 넣어준다
headers = {'Content-Type': 'application/json; charset=utf-8',
           'appKey': appKey}

res = requests.get("https://api2.sktelecom.com/weather/current/minutely?", params=params, headers=headers)
data = res.json()
weather = data.get('weather').get('minutely')[0]
wind = weather.get('wind')
wdir = wind.get('wdir')
wspd = wind.get('wspd')
print(wdir,wspd)