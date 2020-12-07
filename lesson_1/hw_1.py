#Задание №1

ten = 10
ball = int(input("Сколько в спортзале мячей? "))
name = input("Как тебя зовут? ")
print(type(ball))
if ball > 4 or ball==0:
    print("%s пришел в спорзал , насчитал %d мячей."%(name,ball))
elif ball ==1:
    print("%s пришел в спорзал , насчитал %d мяч."%(name,ball))
else:
    print("%s пришел в спорзал , насчитал %d мяча."%(name,ball))

