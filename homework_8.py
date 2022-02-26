"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
 Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, 
 должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
 """
 class Data:
  def __init__(self, data):
    self.data = data

  @classmethod
  def get_data(cls, data):
    lst = data.split('-')
    data_lst = [int(el) for el in lst]
    return data_lst[0], data_lst[1], data_lst[2]

  @staticmethod
  def verify(day, month, year):
    if 1 <= day <= 31:
      if 1 <= month <= 12:             
        return f'ok'
      else:
        return f'wrong month!'
    else:
      return f'wrong day!'

  def __str__(self):
    return f'Today is {Data.get_data(self.data)}'


d = Data('25 - 2 - 2022')
print(d)
print(Data.verify(25, 2, 2022))
print(d.verify(8, 15, 2022))
print(Data.get_data('25 - 2 - 2022'))
print(d.get_data('25 - 2 - 2022'))


"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, вводимых пользователем. 
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class DivByZero(Exception):
    def __init__(self, txt):
        self.txt = txt

dm = int(input('Введите число (делимое): '))
while True:
  dl = int(input('Введите число (делитель): '))

  try:
      if dl == 0: 
          raise DivByZero("На ноль делить нельзя!")
  except DivByZero as err:
      print(err)
  else:
      res = dm / dl
      print(f"Все хорошо. Результат деления: {res}")
      break

"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами. 
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду «stop». 
При этом скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
 Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента. 
 Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и 
 отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""
class ExcList(Exception):
    def __init__(self, *args):
        self.lst = []

    def numb_error(self):
        while True:
            try:
                n = int(input('Введите число: '))
                self.lst.append(n)
                
                if n == 'q':
                    print('Программа завершена')
                    print(f'В списке следующие элементы: {self.lst} \n ')
                    break    
            except:
                print('Неправильный тип данных!')
                q = input(f'Попробовать еще раз? Y/N ')

                if q == 'Y' or q == 'y':
                    print(x.numb_error())
                elif q == 'N' or q == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'
                
x = ExcList(3)
print(x.numb_error())



"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры, общие для приведённых типов.
 В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
 """
 class Office_equipment:
    def __init__(self, name, price, quantity, pages):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.pages = pages


class Printer(Office_equipment):
    def printing(self):
        return f'печатаем на {self.pages} страницах'


class Scanner(Office_equipment):
    def scaning(self):
        return f'сканируем {self.pages} страниц'


class Copier(Office_equipment):
    def copiering(self):
        return f'копируем {self.pages} страниц'
    
a = Printer('Canon', 3, 200, 7)
print(a.printing())
 
 
"""5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, 
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
class Office_equipment:
    def __init__(self, name, price, amount, pages):
        self.name = name
        self.price = price
        self.amount = amount
        self.pages = pages
        self.product = {}
    
    def __str__(self):
        return f'{self.name} по цене {self.price} в количестве {self.quantity} шт.'


    def accepting(self):
        try:
            d = {'название':[], 'цена':[], 'количество':[], 'ед':[]}
            print('Вводим данные в базу "Товары".','\n')
            name = input('Введите название товара:')
            price = int(input('Введите цену:'))
            amount = int(input('Введите количество:'))
            product = {'название': name, 'цена': price, 'количество': amount}
            print('Список товаров и их характеристики:', '\n')
            for prod in product:
                print(prod,':', product[prod])
        except:
            return f'Ошибка ввода'
            
        
   
    
class Printer(Office_equipment):
    def printing(self):
        return f'печатаем на {self.pages} страницах'


class Scanner(Office_equipment):
    def scaning(self):
        return f'сканируем {self.pages} страниц'


class Copier(Office_equipment):
    def copiering(self):
        return f'копируем {self.pages} страниц'
    
a = Printer('Canon', 3, 200, 5)
print(a.printing())
print(a.accepting())



"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. 
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""
class Complex:
    def __init__(self, x, y, *args):
        self.x = x
        self.y = y
        self.z = 'x + yj'

    def __add__(self, other):
        print(f'Сумма экземпляров равна:')
        return f'z = {self.x+ other.x} + {self.y + other.y}j'

    def __mul__(self, other):
        print(f'Произведение экземпляров равно:')
        return f'z = {self.x * other.x - (self.y * other.y)} + {self.y * other.x}j'

    def __str__(self):
        return f'z = {self.x} + {self.y}j'


z1 = Complex(5, 2)
z2 = Complex(7, 2)
print(z1)
print(z1 + z2)
print(z1 * z2)