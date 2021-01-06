# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
# выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex_Num:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.k = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма k1 и k2 равна')
        return f'k = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение k1 и k2 равно')
        return f'k = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'k = {self.a} + {self.b} * i'


k1 = Complex_Num(3, 8)
k2 = Complex_Num(6, 2)
print(k1)
print(k1 + k2)
print(k1 * k2)
