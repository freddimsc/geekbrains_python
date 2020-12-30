# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


# 5. Продолжить работу над первым заданием. Разработать методы,
# отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.


# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class Store_Mashine:

    def __init__(self, name, price, quantity, article, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.article = article
        self.storage = []
        self.unit_dict = {'Модель': self.name, 'Цена': self.price, 'Количество': self.quantity, 'Артикул': self.article}

    def __str__(self):
        return f'{self.name}, цена {self.price} руб., количество {self.quantity} шт.'

    def add_dict(self):
        try:
            unit_n = input(f'Введите название: ')
            unit_p = int(input(f'Введите цену за ед.: '))
            unit_q = int(input(f'Введите количество: '))
            unit_a = int(input(f'Введите артикул: '))
            uni_input = {'Модель': unit_n, 'Цена': unit_p, 'Количество': unit_q, 'Артикул': unit_a}
            self.storage.append(uni_input)
            print(f'\n {self.storage}')
        except:
            return f'Что-то пошло не так'
        a = input('Для выхода - Q, продолжение - Enter')
        if a == 'Q' or a == 'q':
            print('Наш склад -\n',"\n ".join(map(str,self.storage)))
            return f'Отлично поработали!'
        else:
            return Store_Mashine.add_dict(self)

class Printer(Store_Mashine):
    pass


class Scanner(Store_Mashine):
    pass


class Copier(Store_Mashine):
    pass



unit1 = Printer('Sharp', 14000, 19, 100345)
unit2 = Scanner('Samsung', 4000, 8, 105437)
unit3 = Copier('HP', 17000, 7, 123248)
print(unit1)
print(unit2.add_dict())

