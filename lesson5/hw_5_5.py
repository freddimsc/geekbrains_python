#5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summator():
    try:
        with open('sum_num.txt', 'w+') as sum_num:
            line = input('Введите цифры через пробел: \n')
            sum_num.writelines(line)
            numb = line.split()
            print(sum(map(int, numb)))
    except ValueError:
        print('Неправильно ввели числа')
summator()
