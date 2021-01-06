# #1. Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def extract(cls, data):
        date_int = data.split('-')
        return int(date_int[0]), int(date_int[1]), int(date_int[2])

    @staticmethod
    def valid(day, month, year):
            if 1 <= day <= 31 and 1 <= month <= 12 and 2020 >= year >= 0:
                return f'Дата верна'
            return f'Что-то пошло не так'

    def __str__(self):
        return f'Сегодня  {Data.extract(self.data)}'


today = Data('14 - 1 - 2077')
print(today)
print(Data.valid(14, 2, 2023))
print(Data.valid(31, 12, 2020))

