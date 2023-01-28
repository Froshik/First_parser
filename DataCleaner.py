import re

class DataCompiler():
    """Составление данных"""
    def __init__(self, data):
        """Разделяем строку на данные"""
        self.data = data
        self.wind = self.data[-3:-1]
        self.rainfall = self.data[-9:-5]
        self.wet = self.data[-12:-8]
        self.temp = self.data[-16:-12]
        self.cityName = self.data[:-13]

    def string_format(self):
        """Убираем лишние символы"""
        info = []
        for data in (self.temp, self.wet, self.rainfall, self.wind):
            info.append(Cleaner.cutter_num(data))
            name = Cleaner.cutter_name(self.cityName)
        return name, info

class Cleaner():
    """Отчистка входящих данных"""

    def cutter_num (garbage):
        var=re.sub("[%|°| ]","", garbage)
        replaced = (var.translate({ord(i): None for i in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'}))
        return replaced

    def cutter_name (var):
        city_name ="".join(c for c in var if c.isalpha())
        return city_name