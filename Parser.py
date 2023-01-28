import requests
import json
from DataCleaner import DataCompiler
from bs4 import BeautifulSoup

jsondb = "db.json"
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
allDataList = ""
i=0
x = []

while i < 1:
    for data in filteredData:
        city = ""
        db = (data.replace("\t", ""))
        db = (db.replace("\n", ""))
        city =  city + db + " "
        dataPost = DataCompiler(city)
        print(city)
        print(dataPost.string_cutter())
        i = i + 1
        break

    
#         wind = city[-3:-1]
#         wind = (wind.translate({ord(i): None for i in 'м'}))
#         rainfall = city[-9:-5]
#         rainfall = (rainfall.translate({ord(i): None for i in '%'}))
#         rainfall = (rainfall.replace(" ",""))
#         wet = city[-12:-8]
#         wet = wet.split("%")[0]
#         wet = (wet.translate({ord(i): None for i in '° '}))
#         temp = city[-15:-10]
#         temp = temp.split("°")[0]
#         temp = (temp.translate({ord(i): None for i in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'}))
#         cityName = city[:-14]
#         cityName = (cityName.translate({ord(i): None for i in '-+12'}))
#         cityName = (cityName.replace(" ",""))
#         allData = cityName + " " + temp + " " + wet + " " + rainfall + " " + wind
#         allDataList = (f'{allData.split()}')
#         dataTxt.write(allDataList + "\n")
#         i = i + 1
#         x.append(allData)
# print (x)
# print("База данных обновлена")
# dataTxt.close
# with open (jsondb ,"w", encoding='utf-8') as f:
#          json.dump(x, f, ensure_ascii= False)
#          f.close