#1 задание
def func():
    example = {
        'iceberg': ['cold', 15, {'a', 'b'}, 33.98, 15/2, False],
        'fire': ['hot', 46, ['cha', 'ching'], 81.13],
        'earth': ['solid', 100, (13, 31, 1), 90.01, {'b':'c'}]
        }
    summ = 0
    elements = ['fire', 'storm', 'cloud', 'iceberg', 'volcano', 'earth']
    for i in elements:
        try:
            for b in example[i]:
                try:
                    summ += b
                except TypeError:
                    continue
        except KeyError:
            print(f"Ключа {i} нет в списке")
        else:
            print(f"{i} - {summ}")
            summ = 0    

func()

#2 Задание

import random

names = ['dhhgfjjhsa.txt', 'hhdsdahffh.txt', 'afdgdhjsds.txt', 
	'sggjghddss.txt', 'fjdjgdghdf.txt', 'sjssahjfga.txt', 
	'agsgdjhhfj.txt', 'gafadhadda.txt', 'hdagajfhhj.txt', 
	'fhjhafhdfa.txt']

def rewrite():
    for i in names:
        try:
            new_file = open(i, 'r')
            new_file.close()
        except FileNotFoundError:
            print(f'Файл {i} не найден')
        else:
            new_file = open(i, 'a')
            new_file.write('Billybek Djabrailov')
            new_file.close()

rand_file = random.choice(names)
f = open(rand_file, 'a')
f.close()
rewrite()


#3 Задание

spendings = [140, 30, 999, 145, 538, 878, 901, 613, 471, 286, 147, 90]
income = [300, 40, 0, 4000, 8911, 73, 85, 0, 9000, 941, 658, 190]

summ = 0
for i in range(12):
    try:
        a = spendings[i] / income[i]
    except ZeroDivisionError:
        a = 0
    else:
        summ += a
summ /= 12
print(f"годовой коэфициент: {summ}")
