#2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

list = [324, 2, 3, 44, 1, 233, 3, 10,20, 1, 21, 123, 52,76]

new_list = [int(el) for i, el in enumerate(list) if list[i - 1] < list[i]]
print(f'Мой список {list}')
print(f'Новый список {new_list}')


