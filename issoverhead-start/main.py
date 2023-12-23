import requests
from datetime import datetime
import smtplib

"51.507351 "
"-0.127758 "
MY_LAT = 0
MY_LONG = 130 
MY_MAIL = "your mail"
MY_PASSWORD = "your app password"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
#current time in the 24h format 
time_now_hour = time_now.hour

#current time in the 12h format 
time_now_hour_12 = str(time_now_hour)

time_now_hour_12 = time_now.strftime("%I").lstrip("0")

print(MY_LAT)
print(iss_latitude)

print(MY_LONG)
print(iss_longitude)



#If the ISS is close to my current position
if  iss_latitude -5 < MY_LAT < iss_latitude + 5 and iss_longitude - 5 < MY_LONG < iss_longitude + 5:
  if  sunset < time_now_hour or  time_now_hour_12 < sunrise:
    # and it is currently dark
    # Then send me an email to tell me to look up.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        #secure 
        connection.starttls()
        #login 
        connection.login(user=MY_MAIL, password=MY_PASSWORD)

        #sendMail
        connection.sendmail(from_addr=MY_MAIL, to_addrs=MY_MAIL, msg="Subject: Iss in the Sky, look up \n\n Look up, the iss should be over your head")
    print("mail send")


# BONUS: run the code every 60 seconds.



