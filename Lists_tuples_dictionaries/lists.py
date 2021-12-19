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

# numbers = [23, 42, 1, 54, 21, 94]
# numbers.sort()
# print(numbers)
# print(sorted(numbers))

# numbers = [23, 42, 1, 54, 21, 94]
# print(min(numbers))
# print(max(numbers))

# name1 = ["Aleftina", "Zina", "Inakentiy"]
# name2 = name1
# print(name1)
# print(name2)
# name2.append("Kuki")
# print(name1)
# print(name2)

# import copy
#
# name1 = ["Aleftina", "Zina", "Inakentiy"]
# name2 = copy.deepcopy(name1)
# print(name1)
# print(name2)
# name2.append("Kuki")
# print(name1)
# print(name2)

# names = ["Alex", "Lola", "Olga", "Dima", "Nikolas", "Yarik"]
# print(names[:3])
# print(names[2:5])
# print(names[1:5])

# names1 = ["Igor", "Ignat", "Akaki"]
# names2 = ["aniel", "Zoran", "Pedja"]
# user3 = names1 + names2
# print(sorted(user3))

# users = [
#     ["Lida", 29],
#     ["Kuki", 21],
#     ["Arsen", 22],
#     ["Srgan", 45]
# ]
# print(users[2][0])

# users = [
#     ["Lida", 29],
#     ["Kuki", 21],
#     ["Arsen", 22],
#     ["Srgan", 45]
# ]
#
# for user in users:
#     for i in user:
#         print(i, end=" | ")

