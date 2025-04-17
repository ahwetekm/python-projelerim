import requests

base_url = "http://api.weatherapi.com/v1/forecast.json?key=685e2c31dd0c434e92d144440251004&q="
sehir = input("Şehir giriniz (Önek: New_York, Istanbul, Ankara, Çankırı, Tokat): ")
url = (base_url + sehir + "&days=1&aqi=no&alerts=no")
gelen = requests.get(url)
veri = gelen.json()
durum = veri['current']['condition']['text']
derece = veri['current']['temp_c']
if durum == "Partly cloudy":
  durum = "Parçalı Bulutlu"
elif durum == "Clear":
  durum = "Açık"
elif durum == "Sunny":
  durum = "Güneşli"
elif durum == "Moderate or heavy snow showers":
  durum = "orta veya yoğun kar yağışlı"
elif durum == "Heavy snow":
    durum = "Yoğun kar yağışlı"
elif durum == "Overcast":
    durum = "Bulutlu"
print(sehir," şuan ",str(round(derece, ))," derece ve ",durum)
