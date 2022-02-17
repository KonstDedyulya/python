""" 1. Создать класс TrafficLight (светофор).
 
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
 
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time
class TrafficLight:
  __color = ['red', 'yellow', 'green' ]
  
  def running(self):
    
    n = 0
    while n != 2:
      sec = 0
      print()
      print(f'Traffic Light is {TrafficLight.__color[0]}')
      while sec != 7:
        time.sleep(1)
        sec += 1
        print('#', end='')
      
      print()
      print(f'Traffic Light is {TrafficLight.__color[1]}')
      sec = 0
      while sec != 2:
          time.sleep(1)
          sec += 1
          print('#', end='')
      
      print()
      print(f'Traffic Light is {TrafficLight.__color[2]}')
      sec = 0
      while sec != 10:
        time.sleep(1)
        sec += 1
        print('#', end='')    
      
      n += 1



a = TrafficLight()
a.running()

""" 2. Реализовать класс Road (дорога).
 
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина х ширина х масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.
 
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""
class Road:
  def _init_ (self, _lengh, _width):
    self._lengh = lengh
    self._width = width
  
  def asphalt_mass(self, _lengh, _width, weight, depth):
    return print(f'{int(((_lengh * _width) * weight * depth) / 1000)} т.') 

a = Road()
a.asphalt_mass(20, 5000, 25, 5)

""" 3. Реализовать базовый класс Worker (работник).
 
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""
class Worker:
  def __init__(self, name, surname, position, wage, bonus):
    self.name = name
    self.surname = surname
    self.position = position
    self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
  def description(self, name, surname, position, wage, bonus):
    super().__init__(self, name, surname, position, wage, bonus)

  def get_full_name(self):
    return self.name + ' ' + self.surname
  def get_total_income(self):
    return self._income.get('wage') + self._income.get('bonus')
 
    
a = Position('Alex', 'Vihrov', 'Senior scientist', 3000, 500)
print(a.get_full_name())
print(a.get_total_income())

""" 4.Реализуйте базовый класс Car.
 
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
 
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""

class Car:
  def __init__(self, speed, color, name, is_police):
    self.speed = speed
    self.color = color
    self.name = name
    self.is_police = is_police

  def go(self):
    return print(f'{self.name} поехал')

  def stop(self):
    return print(f'{self.name} остановился')

  def turn_left(self):
    return print(f'{self.name} повернул влево')

  def turn_right(self):
    return print(f'{self.name} повернул вправо')
  
  def show_speed(self):
    return print(f'Скорость {self.speed} км/ч')


class TownCar(Car):
  def __init__(self, speed, color, name, is_police):
    super().__init__(speed, color, name, is_police)
    
  def show_speed(self):
    if self.speed > 60:
      print(f'{self.name} превышает скорость!')


class SportCar(Car):
  def __init__(self, speed, color, name, is_police):
    super().__init__(speed, color, name, is_police)
    

class WorkCar(Car):
  def __init__(self, speed, color, name, is_police):
    super().__init__(speed, color, name, is_police)
    
  def show_speed(self):
    if self.speed > 40:
      print(f'{self.name} превышает скорость!')


class PoliceCar(Car):
  def __init__(self, speed, color, name, is_police):
    super().__init__(speed, color, name, is_police)
    

a = Car(30, 'красный', 'рено', False)
b = TownCar(65, 'синий', 'ситроен', False)
c = SportCar(180, 'белый', 'BMW', False)
d = WorkCar(35, 'серебристый', 'тойота', False)
e = PoliceCar(75, 'белый', 'лада', True)


b.turn_left()
b.show_speed()

c.go()
c.turn_right()
c.stop()

""" 5.Реализовать класс Stationery (канцелярская принадлежность).
 
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery:
  def __init__(self, title):
    self.title = title
  
  def draw(self):
    return print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
  def __init__(self, title):
    super().__init__(title)
  
  def draw(self):
    return print(f'Используем {self.title}!')


class Pencil(Stationery):
  def __init__(self, title):
    super().__init__(title)
  
  def draw(self):
    return print(f'Используем {self.title}!')


class Handle(Stationery):
  def __init__(self, title):
    super().__init__(title)
  
  def draw(self):
    return print(f'Используем {self.title}!')



a = Pen('ручка')
a.draw()

b = Pencil('карандаш')
b.draw()

c = Handle('маркер')
c.draw()


