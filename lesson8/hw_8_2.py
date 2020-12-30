# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class Div_zero:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def rule_zero(a, b):
        try:
            return (a / b)
        except ZeroDivisionError:
            return (f"На ноль делить нельзя")

    def __str__(self):
        return str(Div_zero.rule_zero(self.a, self.b))


div = Div_zero(777, 77)
print(div.rule_zero(7, 0))
print(div)
