#1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

a = int(input("Введите произвольное число делимое:  "))
b = int(input("Введите произвольное число делитель:  "))
def func_1(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Error!')

print(f'Ответ : {func_1(a, b)}')
