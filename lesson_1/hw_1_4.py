# Задание № 4
n = int(input("Введите число : "))
maximum = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > maximum:
        maximum = n % 10
    if n > 9:
        continue
    else:
        print(maximum)
        break