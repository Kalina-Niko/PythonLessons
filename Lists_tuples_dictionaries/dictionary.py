# users = {1: "Nikita", 2: "Galina", 3: "VoLodimir"}  #Создание словаря! (перед двоеточием КЛЮЧ, после ЗНАЧЕНИЕ!)
# print(users)

# country = {"Ukraine": "Kyiv", "Usa": "Washington", "Russia": "Moscow"}  # Создание dictionary(словарь).
# print(country)

# Создание словаря со всеми типами данных.
# dictionary_objects = {1: 32, 2: 32.2, 3: True, 4: [1, 2, 4], 5: (2, 21, 12), 6: "Marja Ivanovna", 7: {1: 32, 2: 45}}
# print(dictionary_objects)

# objects = {}  # Создание пустого словаря.
# print(objects)
# print(type(objects)) # распознает пустые словари в отличии от тайплов

# objects = dict()
# print(type(objects))  # Вычесление типа данных.

# user_list = [   # Создвние листа, со вложенными листами.
#     [380662223311, "nik"],
#     [380961112233, "jarik"],
#     [380669991122, "maxim"]
# ]
# print(user_list)
#
# user_dict = dict(user_list)  # Конвертирование листа в словарь!
# print(user_dict)

# user_tuple = (
#     (380973231122, "Volodya"),
#     (380672212233, "Ljuda"),
#     (380673213445, "Polina")
# )
#
# user_dictor = dict(user_tuple)  # конвертирование тайпла в словарь!
# print(user_dictor)

# experiment_dict = {
#     "Yashaka": 32,
#     "Lolka": 17,
#     "Ihor": 21,
#     "Gogik": 25
# }
# try:
#     exp_dict = input("Введите ключ: ")
#     print(experiment_dict[exp_dict])  # Вычесление значения по ключу, с учетом принятия ключа от пользователя.
# except KeyError:  # Исключение в случае ввода несуществующего ключа!
#     print("Ключ введен не правильно!")
# finally:
#     print("Програма завершена!")

