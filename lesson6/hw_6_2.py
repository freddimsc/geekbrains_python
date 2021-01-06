#2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
#Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width


class MassRoad(Road):
     def __init__(self, length, width, weight, thickness=1):
         super().__init__(length, width)
         self.weight = weight
         self.thickness = thickness

     def calculat(self):
         formula = self._length * self._width * self.weight
         if self.thickness > 1:
             return formula * self.thickness
         return formula # если число см толщины полотна = 1 см

road = MassRoad(20,30,45)
print(road.calculat())
