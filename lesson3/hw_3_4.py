#4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.



#Правильное решение только деление на 2!
#def my_func(x, y):
 #   for i in range(abs(y+1)):
   #     x *= x
    #return 1 / x

#print(my_func(7, -4))


#Правильное решение!
def power(base,pwr):
    res = 1
    for n in range(pwr):
        res *= base
    return 1 / res

print(power(7,4))