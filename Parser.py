import requests
import json
from DataCleaner import DataCompiler
from bs4 import BeautifulSoup

jsondb = "Data/db.json"
filteredData = []

url = "https://pogoda.mail.ru/country/russia/"

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text, "html.parser")

table = soup.find_all('li', {'data-logger': "pogoda__ForecastCountryCityItem"})
for data in table:
    if data.find("span", {"class": "city-list__val"}) is not None:
        filteredData.append(data.text)

x = []
for data in filteredData:
    city = ""
    db = (data.replace("\t", ""))
    db = (db.replace("\n", ""))
    city =  city + db + " "
    dataPost = DataCompiler(city)
    print(city)
    x.append(dataPost.string_format())

with open (jsondb ,"w", encoding='utf-8') as f:
    json.dump(x, f, ensure_ascii= False)
    f.close