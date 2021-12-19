# numbers = [1, 2, 3, 4, 5]  # создаем лист и заполняем его элементами!
# print(type(numbers))  # Проверка типа данных листа!

# numbers1 = [] # Создаем пусты листы!
# numbers2 = list() # Создаем пусты листы!

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # создаем лист и заполняем его элементами!
# numbers2 = list(numbers) # Создаем новый лист и записываем в него значение numbers
# numbers3 = numbers  # Создаем новый лист и записываем в него значение numbers ( АЛЬТЕРНАТИВНЫМ СПОСОБОМ )
# print(numbers)
# print(numbers2)
# print(numbers3)

# numbers = [1, 2, 3, 4, 5] # создаем лист и заполняем его элементами!
# print(numbers)
# print(numbers[4]) # Вычесление значения из листа с помощью индекса!

# numbers = [1, 5, 22, 21, 55, 12]
# print(numbers[4])

# numbers = [23, 43, 12, 95, 21, 55]  # создаем лист и заполняем его элементами!
# print(numbers)
# numbers[4] = 100  # Замещение значения в листе с помощью индекса!
# print(numbers)

# numbers = [5] * 6  # Клонирует значение в листе на то число которое умножает!
# print(numbers)

# numbers = list(range(5, 10))  # прогон от мин до макс ( от 5 до 10)
# print(numbers)

# objects = [1, 2.5, "привет", True, [1, 2, 3, 4], []]  # создание листа и наполнение его разными типами данных!
# print(objects)
# print(objects[4])  # ВЫвод значения из листа с помощью индекса!

# objects = [1, 2.5, "привет", True, [1, 2, 3, 4], []]
# print(objects)
#
# for i in objects:
#     print(i)
#
# counter = 0
# while counter < len(objects):
#     print(objects[counter])
#     counter += 1

# numbers = [1, 21, 54, 21, 43, 2, 21]
# print(numbers)
# numbers.append("Nikita")  # добавляем в конец элемент !
# print(numbers)
# print(numbers.index(21))  # Вычесление индекса по значению!
# numbers.pop(7)  # Удаление элемента по индексу
# print(numbers)
# numbers.reverse()  # Зеркальное отображение ЛИСТА!
# print(numbers)
# numbers.sort()  # сортирует по возрастанию
# print(numbers)
# numbers.count(21)  # Считает повторение значения в листе!
# print(numbers.count(21))
# numbers.insert(-2, "Nikita")  # Вставляет значение по индексу, в данном примере показано со знаком МИНУС!
# print(numbers)
# numbers.pop(5)  # Удаление по индексу НИКИТА для дальнейшей работы с функциями!
# print(numbers)
#
# print("Длина нашего листа:", len(numbers))  # Вычесление количества значений или по правильному длины листа!
# print(sorted(numbers))  # Сортировка от меньшего к большему!
# print(min(numbers))  # Вычесление меньшего значения !
# print(max(numbers))  # Вычесление найбольшего значения !

# names = ["Nik", "Serge", "Ivan", "Katya", "Dima"]
# delete_name = input("Введите имя которое хотите удалить: ")
# if delete_name in names:
#     names.remove(delete_name)  # Удаляет значение, по значению!
# print(names)

# names = ["Nik", "Serge", "Ivan", "Katya", "Dima", "Dima", "Dima"]


# def dell(names_user):
#     delete_name = input("Введите имя которое хотите удалить: ")
#     index_delete_user = names_user.index(delete_name)
#     names_user.pop(index_delete_user)
#     return names_user
#
#
# print(dell(names))

# def clone(names_user):
#     search_name = input("Введите имя: ")
#     a = names_user.count(search_name)
#     print("Слово", search_name, "в листе", names_user, "повторяется", a, "раз(а)!")
#
#
# clone(names)

# numbers = [23, 42, 1, 54, 21, 94]    # создание листа и наполнение элементами
# numbers.sort()    #  метод сортировки значений
# print(numbers)
# print(sorted(numbers)) #  функция сортировки значений

# numbers = [23, 42, 1, 54, 21, 94]  # создание листа и наполнение элементами
# print(min(numbers)) # Вывод минимального значения
# print(max(numbers)) # # Вывод максимального значения

# name1 = ["Aleftina", "Zina", "Inakentiy"] # создание листа и наполнение элементами
# name2 = name1  # создание копии листа которые указывают на один и тот же объект
# print(name1)
# print(name2)
# name2.append("Kuki")  # Добавления значения в ОБА листа
# print(name1)
# print(name2)

# import copy  # Импортирование библиотеки  в наш файл
#
# name1 = ["Aleftina", "Zina", "Inakentiy"] # создание листа и наполнение элементами
# name2 = copy.deepcopy(name1)  # Использование метода библиотеки
# print(name1)
# print(name2)
# name2.append("Kuki")  # Добавление значения в один листов ( name2)
# print(name1)
# print(name2)

# names = ["Alex", "Lola", "Olga", "Dima", "Nikolas", "Yarik"]  # создание листа и наполнение элементами
# print(names[:3])  # Вывод обрезаного листа
# print(names[2:5]) # Вывод обрезаного листа  от ольги до ярика
# print(names[1:5]) # Вывод обрезаного листа  от Лолы до ярика

# names1 = ["Igor", "Ignat", "Akaki"]  # создание листа и наполнение элементами
# names2 = ["aniel", "Zoran", "Pedja"] # создание листа и наполнение элементами
# user3 = names1 + names2 # соедение листов
# print(sorted(user3)) # сортировка соедененных листов

# users = [  # создание общего листа
#     ["Lida", 29],
#     ["Kuki", 21],
#     ["Arsen", 22],
#     ["Srgan", 45]  # создание листа в листе
# ]
# print(users[2][0]) # Вывод значений

# users = [ # создание общего листа
#     ["Lida", 29],
#     ["Kuki", 21],
#     ["Arsen", 22],
#     ["Srgan", 45]  # создание листа в листе
# ]
#
# for user in users: # циклом for прогон users и помещение в user
#     for i in user: # прогон каждого отдельно из user
#         print(i, end=" | ") # Вывод который после каждого элемента ставит верт.полоску



