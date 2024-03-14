import requests
from datetime import datetime


def weather(city_name):
    parametres = {
        "q": city_name,
        "appid": "b01e7608c07f15c54ff9d9b64d478705",
        "units": "metric"
    }

    res = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parametres).json()
    temp = res['main']['temp']
    temp_max = res["main"]["temp_max"]
    temp_min = res["main"]["temp_min"]
    city = res['name']
    description = res['weather'][0]['description']
    description = description
    wind_deg = res["wind"]["deg"]
    wind = res['wind']['speed']
    sunrise = datetime.utcfromtimestamp(res['sys']['sunrise'] + res['timezone']).strftime("%Y.%d.%m  %H:%M:%S")
    sunset = datetime.utcfromtimestamp(res['sys']['sunset'] + res['timezone'])
    info = f"""🏙 {city} shaxrida
     Ob havo
 {description}
⛅️ Harorat {temp} °C
⛅️ Eng yuqorisi  {temp_max} °C
⛅️ Eng pasi {temp_min} °C

💨 shamol {wind_deg} dan esadi tezligi {wind} m/s  

☀️ quyosh chiqishi {sunrise}
🌇 quyosh botishi {sunset}

"""
    print(info)
    print("-" * 20)