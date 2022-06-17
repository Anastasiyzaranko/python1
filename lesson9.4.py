# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, ):
        print(" машина поехала")

    def stop(self):
        print(" машина остановилась")

    def turn(self, direction):
        print(" машина повернула", direction)

    def show_speed(self):
        print(" текущая скорость автомобиля ", self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(" Вы превысили скорость ")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(" текущая скорость автомобиля ", self.speed)
        if self.speed > 40:
            print(" Вы превысили скорость ")


class PoliceCar(Car):
    pass


t = TownCar(100, "синий", "мазда", False).show_speed()
s = SportCar(150, "красный", "ауди", False).show_speed()
w = WorkCar(200, "зеленый", "бмв", True).show_speed()
p = PoliceCar(70, "голубой", "фольксваген", True).show_speed()

a = Car(100, "синий", "мазда", None)
print(a.go())
print(a.stop())
print(a.turn("к заправке"))
