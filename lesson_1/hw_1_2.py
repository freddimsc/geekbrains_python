#Задание 2
time = int(input("Сколько Вам необходимо в секундах потребуется почистить апельсин? "))
minutes = 0
hour = 0
seconds = 0
if time >= 60:
       minutes = time//60
       seconds = time % 60
       if minutes >= 60:
            hour = minutes//60
            minutes = minutes % 60
else:
    seconds = time
print( "Вам необходимо %02d:%02d:%02d времени."%(hour,minutes,seconds) )