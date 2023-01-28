import json


#"assets\city.txt"
ask = input("")
with open("data\db.json", encoding="utf-8") as russianCities:
    data = russianCities.read()
    json_data = json.loads(data)
for line in json_data:
    lineAsStr = str(line)
    search = lineAsStr.find(ask)
    if search > 0:
        answer = line
        print(line)
russianCities.close