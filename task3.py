# pip install requests(in your terminal)
import requests
from pprint import pprint
from datetime import datetime
url = "https://api.open-meteo.com/v1/forecast?latitude=13.754&longitude=100.5014&hourly=temperature_2m,relativehumidity_2m&timezone=Asia%2FBangkok"

result = requests.get(url)

pprint(result.json())
values = result.json()

print(values["latitude"])
x = values["hourly"]["temperature_2m"]
print(values["hourly"]["temperature_2m"])

max_temperature = max(x)

myindex = x.index(max_temperature)
print(myindex)

mytimes = values["hourly"]["time"]
print(mytimes)
mytime = mytimes[myindex]
print(mytime)


hottest_day = datetime.strptime(mytime,'%Y-%m-%dT%H:%M')
print(hottest_day)