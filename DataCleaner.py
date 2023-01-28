class DataCompiler():
    """Составление данных"""
    def __init__(self, data):
        self.data = data
        self.wind = ""
        self.rainfall = ""
        self.wet = ""
        self.temp = ""
        self.cityName = ""

    def string_cutter(self):
        """Будем разделять полученную строку на данные"""
        self.wind = self.data[-3:-1]
        return self.wind


class Cleaner():
    """Отчистка входящих данных"""

    def __init__(self, garbage):
        self.garbage = garbage

    def refuse(self):
        return self.garbage + "ggg"
