#. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
my_list = [7, 5, 3, 3, 2]
number = int(input("Ведите новый элемент рейтинга:  "))
for i in my_list:
        my_list.append(number)
        my_list = sorted(my_list, reverse=True)
        break
print(my_list)