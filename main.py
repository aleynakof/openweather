import requests

import json

import converter
from multiple_replace import multiple_replace

city = input("insert a city name").replace("İ", "i").lower()
print(city)
api_request = requests.get("http://api.openweathermap.org/data/2.5/"
                           "weather?q=" + city + "&appid=******************")
print(api_request)

weather = {
    "Clouds": "Bulutlu",
    "Clear": "Açık",
    "Rain": "Yağmurlu"
}

# json document
result = json.loads(api_request.content)

print(result)
print("Temperature in ", city, " is {} K".format(result["main"]["temp"]))
print("Temperature in ", city, " is {} C".format(round(converter.kelvin_to_celcius(result["main"]["temp"]), 2)))

print("Weather in ", city, weather[result["weather"][0]["main"]])

print("------------------------------------")
# key: 24bb5a00705b2420901490c95519ab0b

# sehir = input("Şehri giriniz:")
# sehir = sehir.capitalize()
#
# api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+sehir+"&appid=24bb5a00705b2420901490c95519ab0b")
#
# # result dönen JSON dökümanıdır.
# result = json.loads(api_request.content)
#
#
# #print(result)
#
# hava_sozlu = {
#     "Clouds": "Bulutlu",
#     "Clear": "Açık",
#     "Rain": "Yağmurlu"
# }
#
# print(sehir + " sıcaklığı: {} K".format(result["main"]["temp"]))
# print(sehir + " sıcaklığı: {0:.2f} C".
#       format(cevir.kelvin_to_celcius(result["main"]["temp"])))
# print(sehir + " sıcaklığı: {} C".
#       format(round(cevir.kelvin_to_celcius(result["main"]["temp"]), 2)))
# print(sehir + " sıcaklığı: {0:.2f} F".
#       format( cevir.kelvin_to_fahrenheit(result["main"]["temp"])))


# print(sehir + " havası(sözlü):", hava_sozlu[result["weather"][0]["main"]])
