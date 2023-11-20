import time

import requests
import datetime as dt
import smtplib

MY_LAT = 12.971599
MY_LONG = 77.594566
my_email = "winmaktum@gmail.com"
my_password = "avvj nmmx vofn fimc"


# if the ISS is close yo my current postion
def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  # instead of raising individual exception for status code this will do that for us.
    data = response.json()
    print(data)

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    # Your position is withing +5 or -5 degrees of the ISS position
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        return True


# we  need to add API parameters
parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}


# if it is currently dark
def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # print(sunrise)
    # print(sunset)
    time_now = dt.datetime.now().hour
    if sunrise < time_now < sunset:
        return True


# Then email me to tell me to look up
while True:
    time.sleep(60)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:Look Up\n\nThe ISS is above you in "
                                                                       "the sky")


# BONUS: run the code every 60 seconds
