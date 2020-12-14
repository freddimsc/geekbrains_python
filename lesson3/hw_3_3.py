#3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a,b,c):
    list = [a,b,c]
    list.remove(min(a,b,c))
    return sum(list)
print(my_func(14,2,26))
