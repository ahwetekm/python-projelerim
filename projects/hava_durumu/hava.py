import requests

url = "http://api.weatherapi.com/v1/forecast.json?key=685e2c31dd0c434e92d144440251004&q=Istanbul&days=1&aqi=no&alerts=no"
gelen = requests.get(url)
veri = gelen.json()
ist_durum = veri['current']['condition']['text']
ist_derece = veri['current']['temp_c']
if ist_durum == "Partly cloudy":
  ist_durum = "Parçalı Bulutlu"
elif ist_durum == "Clear":
  ist_durum = "Açık"
print("Istanbul için hava durumu (genel)")
print("Derece: ", ist_derece)
print("Durum: ", ist_durum)

