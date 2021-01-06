#3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
with open('spisok.txt', 'r') as my_file:
    workers = {}
    my_list = my_file.read().split('\n')
    for i in my_list:
        surname, wage = i.split(',')
        workers[surname] = wage
        if int(wage) < 20000:
            print(f'{surname}: зарплата меньше 20000 рублей')
    my_file.seek(0)
    l =[]
    for i in my_list:
        surname, wage = i.split(',')
        workers[surname] = wage
        l.append(wage)
    print(f'Средний оклад {sum(map(int, l))/len(l)} рублей')