""" 1. Создать программный файл в текстовом формате, записать в него построчно данные, 
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.
"""
f = open(r'c:\Users\konst\homework5\test1.txt', 'w')
while True:
    string = input()
    if string == '':
        break
    else:
        f.write(string + '\n')
f.close()

""" 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, 
выполнить подсчёт строк и слов в каждой строке.
"""
strs = []
f = open(r'c:\Users\konst\homework5\test1.txt', 'r')
s = f.readlines()
l = 0
for line in s:
    l += 1
    strs = line.split()
    w = len(strs)
    print(f'Слов в строке {l}: {w}')

f.close()
print(f'Всего строк в файле: {l}')

""" 3. Создать текстовый файл (не программно).
 Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк)
 . Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии 
 этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
 Пример файла: Иванов 23543.12 Петров 13749.32
 """
 
 salary = []
surname = []
with open(r'c:\Users\konst\homework5\test1.txt', 'r') as f:
    #content = f.read()
    s = f.readlines()
    for line in s:
        strs = line.split()
        salary.append(float(strs[1]))
        surname.append(strs[0])
big_salary = [surname[i] for i in range(len(salary)) if salary[i] > 20000]
print('Следующие сотрудники зарабатывают неприлично много:')
for v in big_salary:
    print(v) 
print('\n', 'Средний доход всех сотрудников:', sum(salary) / len(salary))

""" 4. Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4 
Напишите программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. Новый блок строк 
должен записываться в новый текстовый файл.
"""
rus_numb = ['Один', 'Два', 'Три', 'Четыре']
rus_line = []
i = 0
out = open(r'c:\Users\konst\homework5\output.txt', 'w')
with open(r'c:\Users\konst\homework5\test2.txt', 'r', encoding="utf-8") as f:
    for line in f:
        rus_line = line.split()
        rus_line.remove(rus_line[0])
        rus_line.insert(0, rus_numb[i])
        string = ''.join(rus_line)
        i += 1
        out.write(string + '\n')
out.close()

""" 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
f = open(r'c:\Users\konst\homework5\test3.txt', 'w+')
string = [str(i) for i in range(31)]
#print(string)
for numb in string:
    f.write(numb + ' ')
f.close()

f = open(r'c:\Users\konst\homework5\test3.txt', 'r')
for line in f:
    string = line.split()

lst = [int(numb) for numb in string]
print('Сумма чисел в файле =', sum(lst))

""" 6. Сформировать (не программно) текстовый файл. 
В нём каждая строка должна описывать учебный предмет и наличие лекционных, 
практических и лабораторных занятий по предмету. 
Сюда должно входить и количество занятий. Необязательно, 
чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий 
по нему. Вывести его на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
d = {}
num_list = []
num = ''
f = open(r'c:\Users\konst\homework5\test6.txt','r', encoding="utf-8")

for line in f:
    for el in line:
        if el.isdigit() and el != '(':
                num += el
        elif el == '(':
            num_list.append(int(num))
            num = ''
    string = line.split()
    for el in string:
        if el not in d:
            d[string[0]] = sum(num_list)
    num_list = []
                                                         
print(d)
f.close()

""" 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки. 
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков). 
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json
data = []
d1 = {}
d2 = {}
profit = 0
average_profit = 0
lst_profit = []
loss = 0
with open(r'c:\Users\konst\homework5\test7.txt', 'r', encoding="utf-8") as f:
    for line in f:
        string = line.split()
        profit = int(string[2]) - int(string[3])
        if profit < 0:
            loss = abs(profit)
            d1[string[0]] = loss
        else:
            d1[string[0]] = profit
            lst_profit.append(profit)
        
    
    average_profit = sum(lst_profit) / len(lst_profit)    
    d2['average_profit'] =  int(average_profit)  
    data.append(d1)
    data.append(d2)
    print(data)
        
with open("test7.json", "w") as write_f:
    json.dump(data, write_f) 


