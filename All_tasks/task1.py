# x = int(input("Введите количество часов сна ночью: "))
# y = int(input("Введите количество минут сна днем: "))
# b = x * 60
# a = b + y
# print(a)


# x = int(input("Заведи свой будильник в минутах: "))
# print(int(x / 60))
# print(x % 60)

# x = int(input("Скольк минут Вам необходимо для сна: "))
# h = int(input("Во сколько часов Катя ложиться: "))
# m = int(input("Во сколько минут после часов ложиться эта пизда "))
# print(int(x / 60 + (h + m / 60)))
# print(int((((h * 60) + m) +x) % 60))

# try:
#     a = int(input("Введите рекомендуемое время для сна: "))
#     b = int(input("Введите вредность сна в часах: "))
#     h = int(input("Сколько эта рвань спит сейчас: "))
#     if h > a and h < b:
#         print("Это нормально! Долго паскуда проживешь!")
#     if h < a:
#         print("Недосып! ЗДОХНИШЬ ОТ ИНСУЛЬТА С ПРЕДВАРИТЕЛЬНЫМИ ГАЛЮНАМИ")
#     if h > b:
#         print("Пересып! Заебут мигрени!")
# except ValueError:
#     print("Допустим ввод только цифр!")

# from math import sqrt
#
# a = int(input("Введите длину стороны а: "))
# b = int(input("Введите длину стороны b: "))
# c = int(input("Введите длину стороны c: "))
# p = (a + b + c) / 2
# s = sqrt(p * (p - a) * (p - b) * (p - c))
# print(s)


# number = int(input("Введите число: "))
# if - 15 < number <= 12 or 14 < number < 17 or number >= 19:
#     print(True)
# else:
#     print(False, "Регистр символов имеет значение")

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# operation = input("Введите желаемую операцию:")
# try:
#     if operation == "+":
#         print("a + b =", a + b)
#     elif operation == "-":
#         print("a - b =", a - b)
#     elif operation == "/":
#         print("a / b =", a / b)
#     elif operation == "*":
#         print("a * b =", a * b)
#     elif operation == "mod":
#         print("a mod b =", a % b)
#     elif operation == "pow":
#         print("a pow b =", a ** b)
#     elif operation == "div":
#         print("a div b =", a // b)
# except ZeroDivisionError:
#     print("Деленение на ноль")

# from math import sqrt
# class_room = input("Введите тип комнаты: ")
# if class_room == "Треугольник":
#     a = int(input("Введите первое значение: "))
#     b = int(input("Введите второе значение: "))
#     c = int(input("Введите третье значение: "))
#     p = (a + b + c) / 2
#     s = sqrt(p * (p - a) * (p - b) * (p - c))
#     print(s)
# if class_room == "Прямоугольник":
#     a = int(input("Введите первое значение: "))
#     b = int(input("Введите второе значение: "))
#     s = a * b
#     print(s)
# if class_room == "Круг":
#     r = int(input("Введите радиус: "))
#     p = 3.14
#     s = p * r ** 2
#     print(s)

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
#
# numbers = [a, b, c]
# k = sorted(numbers)
# print(k[2])
# print(k[0])
# print(k[1])

# tiket = input("Введите номер вашего билета: ")
# numbers = []
# for i in tiket:
#     numbers.append(i)
# sum_1 = 0
# sum_2 = 0
# for n in numbers[0:3]:
#     sum_1 += int(n)
# for m in numbers[3:6]:
#     sum_2 += int(m)
# if sum_1 == sum_2:
#     print("Ваш билет счастливый")
# else:
#     print("Неудачник хуев! ")

# b = 0
# while True:
#     a = int(input("Введите число: "))
#     if a != 0:
#         b += a
#     else:
#         break
# print(b)

# while True:
#     a = int(input("Введите число: "))
#     if a < 10:
#         continue
#     elif a > 100:
#         break
#     else:
#         print(a)

# n = input("введите значение: ")
# print(n)
# print(n.split())

# n = input("Введите разные числа (ЧЕРЕЗ ПРОБЕЛЫ): ")
# split_n = n.split()
# a = 0
# for i in split_n:
#     a += int(i)
# print(a)

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# x = []
#
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         x.append(i)
#
# sum_ab = 0
# for i in x:
#     sum_ab += i
#
# print(sum_ab / len(x))

# input_info = input("Введите дичь: ")
# g = ""
# c = ""
#
# for i in input_info:
#     if i == "g" or i == "G":
#         g += i
#     if i == "c" or i == "C":
#         c += i
#
# dlina = len(input_info)
# sum_gc = len(g) + len(c)
# print((sum_gc / dlina) * 100)

# sum_chisel = 0
# pow_chisel = 0

# while True:
#     input_info = int(input("Введите числа: "))
#     sum_chisel += input_info
#     pow_chisel += pow(sum_chisel, 2)
#     if sum_chisel == 0:
#         print("Прием чисел завершен!")
#         break
#
# print(sum_chisel)
# print(pow_chisel)

# y = float(input("Введите значение: "))
#
#
# def check_number(x):
#     if y <= -2:
#         x = 1 - (x + 2) ** 2
#         return x
#     if -2 < y <= 2:
#         x = -(y / 2)
#         return x
#     if 2 < y:
#         x = pow((y - 2), 2) + 1
#         return x
#
#
# print(check_number(y))

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# print(a[0], a[-1])

# n = int(input("Введите целое число: "))
#
#
# def solve(x):
#     summ = x + x * x + x * x * x
#     return summ
#
#
# print(solve(n)

# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
# ]
# for i in numbers:
#     if i == 237:
#         break
#     if i % 2 == 0:
#         print(i)

# a = True
# b = False
# a, b = b, a
# print(a)
#
# a = []
# while len(a) < 10:
#     b = int(input("Добавь число голова говяжья: "))
#     a.append(b)
#
# user = input("Какие числа хотите увидеть парные или непарные:")
# if user == "парные":
#     for i in a:
#         if i % 2 == 0:
#             print(i)
# if user == "непарные":
#     for i in a:
#         if i % 2 != 0:
#             print(i)


# chislo = input("Введите трехзначное слово")
# a = 0
# for i in chislo:
#     a += int(i)
#
# print(a)

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
#
# abc = [a, b, c]
#
# print(max(abc))

# a = int(input("Начало пути: "))
# b = int(input("Конец пути: "))
# x = int(input("Введи блудняк: "))
#
# if a < x < b:
#     print(True)
# else:
#     print(False)

# n = int(input("Введи блудняка: "))
# asd = []
# while True:
#     a = int(input("Введите число: "))
#     if a == 0:
#         break
#     else:
#         asd.append(a)
#
# if n in asd:
#     print(True)
# else:
#     print(False)
#
# print(asd)


#ДЗ
# check_x = int(input("Введите блудняк: "))
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
#
# for i in a and b:
#     if check_x in a and b:
#         print(True)
#     else:
#         print(False)


# check_x = int(input("Введите блудняк: "))
# if 0 <= check_x < 11 or 20 <= check_x < 31:
#     print(True)
# else:
#     print(False)


# numbers = []
# while True:
#     x = int(input("Введите числа:"))
#     numbers.append(x)
#     if x == 0:
#         break
# # numbers.sort(), numbers.pop(0)
# print(len(numbers)-1) # - ТУТ БЫЛО ПРИМенЕНО НАЕБАЛОВО!


# numbers = []
# n = int(input("Введите задание: "))
#
# while True:
#     b = int(input("Введите числа: "))
#     numbers.append(b)
#     if b == 0:
#         break
#
# if n in numbers:
#     print(True)
# else:
#     print(False)

# n = int(input("Введите задание: "))


# def check_n(number):
#     try:
#         local_list = []
#         while True:
#             number_input = int(input("Введите числа: "))
#             local_list.append(number_input)
#             if number_input == 0:
#                 break
#
#         if number in local_list:
#             return True
#         else:
#             return False
#     except ValueError:
#         print("Вводить можно только числовые значения!")
#
#
# print(check_n(number=n))


# n = int(input("Введите главное число: "))
# numbers = []
# while True:
#     number = int(input("Введите числа: "))
#     numbers.append(number)
#     if number == 0:
#         break
#
# num_2 = []
# for i in numbers:
#     if n == i:
#         num_2.append(i)
# print(len(num_2))

# n = int(input("Введите главное число: "))


# def chek_n(number):
#     local_list = []
#     while True:
#         check_n = int(input("Введите числа: "))
#         local_list.append(check_n)
#         if check_n == 0:
#             break
#     num_2 = []
#     for i in local_list:
#         if n == i:
#             num_2.append(i)
#
#     finally_n = len(num_2)
#     return finally_n
#
#
# print(chek_n(number=n))

# local_list = []
# while True:
#     numbers = int(input("Введите числа: "))
#     local_list.append(numbers)
#     if numbers == 0:
#         break
# print(max(local_list))

# def output():
#     local_list = []
#     while True:
#         numbers = int(input("Введите числа: "))
#         local_list.append(numbers)
#         if numbers == 0:
#             break
#     return max(local_list)
#
#
# print(output())
# local_list = []

# while True:
#     check_n = int(input("Введите число: "))
#     local_list.append(check_n)
#     if check_n == 0:
#         break
#
# max_n = max(local_list)
#
# new_ll = []
# for i in local_list:
#     if max_n == i:
#         new_ll.append(i)
#
# print(len(new_ll))


# def chek_max_n():
#     local_list = []
#
#     while True:
#         n = int(input("Введите числа: "))
#         local_list.append(n)
#         if n == 0:
#             break
#
#     max_n = max(local_list)
#     new_ll = []
#     for i in local_list:
#         if max_n == i:
#             new_ll.append(i)
#     return len(new_ll)
#
#
# print(chek_max_n())


# x = int(input())
# y = int(input())
# i = 1
# while x < y:
#     x = x * 1.1
#     i += 1
# print(i)

