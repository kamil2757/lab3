# print("Вычисление площади и периметра прямоугольника по двум сторонам")
# print("1. вычисление площади")
# print('2. вычисление периметра')
#
# while True:
#     v = input("Ваш выбор (1/2): ")
#     if v in ["1", "2"]:
#         v = int(v)
#         break
#     print("Введите 1 или 2!!!")
#
# while True:
#     a = input("Введите 1 число: ")
#     b = input("Введите 2 число: ")
#     try:
#         a = float(a)
#         b = float(b)
#         break
#     except ValueError:
#         print('Нужно ввести числа, а не буквы >:/')
#
# if v == 1:
#     print(f"Площадь: {a * b}")
# else:
#     print(f"Периметр: {a * 2 + b * 2}")
# import string

# print('Калькулятор ИМТ')
# while True:
#     w = input('Введите свой вес (кг): ')
#     h = input('Введите свой рост (см): ')
#     try:
#         w = float(w)
#         h = float(h)
#         if w > 0 and h > 0:
#             break
#         print('вес и рост не могут быть 0 :_')
#     except ValueError:
#         print('Нужно ввести числа!')
# print(f'твой ИМТ: {(w / ((h/100)**2)):.1f}')

# import string
# print('Конвертер систем счисления')
#
# while True:
#     n = input('Введите положительное целое число: ')
#     try:
#         n = int(n)
#         break
#     except ValueError:
#         print("Я же написал: <<целое число>>, попробуй еще разок :)")
#
# while True:
#     cc = input('в какую систему счисления переводить (2/8/16): ')
#     if cc in ['2', '8', '16']:
#         cc = int(cc)
#         break
#     else:
#         print("Введи 2, 8 или 16")
#
# alf = string.digits + string.ascii_uppercase
# def toBase(n, base):
#     res = ''
#     n = abs(n)
#     if n == 0: return "0"
#
#     while n > 0:
#         res += alf[n % base]
#         n //= base
#
#     return res[::-1]
#
# r = toBase(n, cc)
# if n < 0:
#     print("-" + r)
# else: print(r)

# import string
#
# ru_letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
#
# print("Обработка строки")
# s = input('Введите строку: ')
#
# count_letters = 0
# for c in string.ascii_letters + ru_letters:
#     count_letters += s.count(c)
#
# count_numbers = 0
# for n in string.digits:
#     count_numbers += s.count(n)
#
# punct = ".,;:!?\"'()[]{}<>—–-«»„“…”"
# count_punct = 0
# for p in punct:
#     count_punct += s.count(p)
#
# print("кол-во букв: " + str(count_letters), "кол-во цифр: " + str(count_numbers), "кол-во знаков: " + str(count_punct), "кол-во пробелов: " + str(s.count(' ')), sep='\n')


import datetime
print('Работа с датой')

while True:
    y = input('Введите год рождения: ')
    m = input('Введите месяц рождения: ')
    d = input('Введите день рождения: ')
    try:
        y, m, d = int(y), int(m), int(d)
        break
    except:
        print('Введите целые числа')

d1 = datetime.date(y,m,d)
now = datetime.date.today()
print("Вам " + str(int((now - d1).days / 365)) + " годиков")

