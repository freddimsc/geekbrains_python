#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
month = int(input("Какой сейчас месяц :  "))

d ={
    'зима': [1,2,12],
    'весна':[3,4,5],
    'лето':[6,7,8],
    'осень':[9,10,11]
}

for i in d:
     if d[i][0]== month or d[i][1]== month or d[i][2]== month:
         print(f"Сейчас у вас на дворе {i} !")