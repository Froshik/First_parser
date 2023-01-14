import requests
from bs4 import BeautifulSoup

dataTxt = open("data/city.txt", "w", encoding="utf-8")
filteredData = []

url = "https://pogoda.mail.ru/country/russia/"

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text, "html.parser")

table = soup.find_all('li', {'data-logger': "pogoda__ForecastCountryCityItem"})
for data in table:
    if data.find("span", {"class": "city-list__val"}) is not None:
        filteredData.append(data.text)

for data in filteredData:
    city = ""
    allDataList = ""
    db = (data.replace("\t", ""))
    db = (db.replace("\n", ""))
    city =  city + db + " "
    wind = city[-3:-1]
    wind = (wind.translate({ord(i): None for i in 'м'}))
    rainfall = city[-9:-5]
    rainfall = (rainfall.translate({ord(i): None for i in '%'}))
    rainfall = (rainfall.replace(" ",""))
    wet = city[-12:-8]
    wet = wet.split("%")[0]
    wet = (wet.translate({ord(i): None for i in '° '}))
    temp = city[-15:-10]
    temp = temp.split("°")[0]
    temp = (temp.translate({ord(i): None for i in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'}))
    cityName = city[:-14]
    cityName = (cityName.translate({ord(i): None for i in '-+12'}))
    cityName = (cityName.replace(" ",""))
    allData = cityName + " " + temp + " " + wet + " " + rainfall + " " + wind
    allDataList = (f'{allData.split()}')
    dataTxt.write(allDataList + "\n")
    print("База данных обновлена")
    dataTxt.close
