#4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты
# : speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
    def go(self):
        return f'Набираем обороты!'
    def stop(self):
        return f'Кто-то в тачке нажал на тормоз.Цвет тачки {self.color}.Номер не разглядел.'
    def turn(self,direction):
        if direction == 'left':
            return f'{self.name} Поворачивает налево.'
        elif direction == 'right':
            return f'{self.name} Поворачивает направо.'
        else:
            return f'Введите правильный символ: left или right.'
    def show_speed(self):
        return f'Скорость автомобиля в настоящее время {self.speed} км/ч.'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Сбавьте скорость, превышено более 40 км/ч.\n.Ваша {self.name} не потянет скорость {self.speed} км/ч..'
        return super().show_speed()

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Сбавьте скорость, превышено более 40 км/ч.\nВаша {self.name} не потянет скорость {self.speed} км/ч.'
        return super().show_speed()

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
    pass

type_car = {1: PoliceCar,
            2:WorkCar,
            3:SportCar,
            4:TownCar}
mashina = type_car[int(input('Какую вид транспорта  вы выберете:  \n1:PoliceCar\n2:WorkCar\n3:SportCar\n4:TownCar '))]
car = {1: [120,'black','Audi'],
       2: [80,'white','Volvo'],
       3: [50,'red','Lada'],
       4: [140,'darkblue','BMW'],
       5: [280,'green','Bugatti'],
       6: [180,'orange','Suzuki'],
       7: [100,'brown','Mazda']
       }
a = car[int(input('Какую машину вы выберете: \n1:Audi\n2:Volvo\n3:Lada\n4:BMW\n5:Bugatti\n6:Suzuki\n7:Mazda'))]
transport = mashina(a[0],a[1],a[2])
print()
print(transport.go(), transport.turn('left'), transport.show_speed(), transport.turn('right'), transport.stop())
