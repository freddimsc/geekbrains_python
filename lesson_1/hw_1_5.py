# Задание № 5
#Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = float(input("Какая у вас выручка в фирме:  "))
damage = float(input("Какие у вас издержки  фирмы:  "))

profit = revenue - damage
if profit > 0:
    print( "Ваша прибыль составляет {}".format(profit))
    staff = int(input("Сколько в вашей фирме работает сотрудников:  "))
    profit_staff = profit / staff
    print("В расчете на одного сотрудника прибыль фирмы составляет {}".format(profit_staff))
elif profit == 0:
    print("Фирма работает без прибыли, надо задуматься почему.")
else:
    print("Ваш убыток составляет {}".format(profit))