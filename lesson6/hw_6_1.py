#1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
#Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.


from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый',]

    def running(self):
        i = 0

        while i < 3:
            print(TrafficLight.__color[i])
            if self.__color[0] == 'Красный':
                sleep(7)
            elif self.__color[1] == 'Желтый':
                sleep(2)
            elif self.__color[2] == 'Зеленый':
                sleep(4)
            else:
                print('Неправильный порядок режима')
                break
            i += 1

svetofor = TrafficLight()
svetofor.running()
