import requests
import datetime as dt


# we  need to add API parameters
MY_LAT = 51.507351
MY_LONG = -1.127758
parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = dt.datetime.now()
hour = time_now.hour
print(hour)
