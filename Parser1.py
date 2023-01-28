#"assets\city.txt"
ask = input("")
with open("data\city.txt", encoding="utf-8") as russianCities:
        for line in russianCities:
            if line != False:
                search = line.find(ask)
                if search > 0:
                    line1 = (''.join(line))
                    print(line1)
russianCities.close