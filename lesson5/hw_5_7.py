#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
# (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджеры контекста.


import json

with open('firm.txt', 'r') as f_obj:
    profit = {}
    el = 0
    prof_rev = 0
    for i in f_obj:
        name, form, revenue, damage = i.split()
        profit[name] = int(revenue) - int(damage)
        if profit.setdefault(name) >= 0:
            prof_rev = prof_rev + profit.setdefault(name)
            el += 1
    if el != 0:
        prof_aver = prof_rev / el
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'average_profit': round(prof_aver)}
    my_list = [profit, pr]

with open('firm_prof.json', 'w') as prof_js:
    json.dump(my_list, prof_js)
    file_str = json.dumps(my_list)
