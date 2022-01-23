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

# users_numbers = {
#     380995953211: "Kiki",
#     380995953213: "Bimbo",
#     380995953214: "Indiko",
#     380995953210: "Lolka",
#     380995953221: "Koljka"
# }
#
# user = int(input("Введите ключ: "))
# if user in users_numbers:   # прогон словаря, при этом выводит значение по ключу!
#     print(users_numbers[user])
# else:
#     print("Нема ключа!")


# def exp_dict(user):   # функция которая принимает от пользов. ключ, находит значение и выводит его длину!
#     user_phone = int(input("Введите номер: "))
#     if user_phone in user:
#         print(user[user_phone])
#         if len(user[user_phone]) < 5:
#             print("Меньше пяти")
#         else:
#             print("Больше пяти")
#     else:
#         print("Нема нлюча!")
#
#
# exp_dict(users_numbers)


# users_numbers = {
#     380995953211: "Kiki",
#     380995953213: "Bimbo",
#     380995953214: "Indiko",
#     380995953210: "Lolka",
#     380995953221: "Koljka"
# }
#
# user = int(input("Введите ключ: "))
# user_info = users_numbers.get(user, "Элемент не найден!") #Возращает в юзер значение по ключу!
# print(user_info)


# users_info = {
#     "Leon": 380995953221,
#     "Lacy": 380995953222,
#     "Morty": 380995953225
# }
#
# user_give = input("Введите имя: ")
# del users_info[user_give]  # Удаляет из словаря значение по ключу!
# print(users_info)

# users_info = {
#     "Leon": 380995953221,
#     "Lacy": 380995953222,
#     "Morty": 380995953225
# }
# user_give = input("Введите имя:")
# if user_give in users_info:    # Проверяет наличие юзер_гив в юзер_инфо
#     del users_info[user_give]  # удляет по ключу значение из словаря и далее выводит красивый вывод с учетом удал!
#     user_del = user_give
#     print("Пользователь", user_del, "удален!")
# else:
#     print("Элемент не найден!")
# print(users_info)


# users_info = {
#     "Leon": 380995953221,
#     "Lacy": 380995953222,
#     "Morty": 380995953225
# }
# user_give = input("Введите имя: ")
# a = users_info.pop(user_give, "Элемент не найден!")  # Удаление значение методом ПОП, если не удаляется (ЭЛ НЕ НАЙДЕН)
# print(users_info)
# print(a)

# users_info = {
#     "Leon": 380995953221,
#     "Lacy": 380995953222,
#     "Morty": 380995953225
# }
# users_info.clear() # зачистка словаря!
# print(users_info)

# users_info = {
#     "Leon": 380995953221,
#     "Lacy": 380995953222,
#     "Morty": 380995953225
# }
# users_info_2 = users_info.copy() # Копирывание словаря в словарь
# print(users_info)
# print(users_info_2)

# users_info = {
#     "Leon": 380995953221,
#     "Lacy": 380995953222,
#     "Morty": 380995953225
# }
# users_info_2 = {
#     "Galina": 380672123430,
#     "Jhon": 380672123431,
#     "Alina": 380672123432
# }

# users_info.update(users_info_2) # метод которым перетягивается ЮИ2 в ЮИ !
# print(users_info)
# print(users_info_2)

# users_info = {
#     "Leon": 380995953221,
#     "Lacy": 380995953222,
#     "Morty": 380995953225
# }

# for key in users_info:
#     print(key, "-", users_info[key])  # выводит только ключи мето

# for key, value in users_info.items():  # выодит методом итемс и ключи и значение
#     print(key, "-", value)

# for value in users_info.values(): # выводит только значение
#     print(value)

# users = {  # дикшионари - Словари в дикшионари - словарях
#     "Mihalchenko": {  # Ключ словаря
#         "name": "Leon", # Ключ и значение встроеного словаря
#         "phone": 30971112233,
#         "email": "leon.mih@gamil.com"
#     },  # Закрые первого встроеного словаря
#     "Marinovkiy": {
#         "name": "Vladimir",
#         "phone": 380971112244,
#         "email": "vova@gmail.com"
#     },
#     "Dubinko": {
#         "name": "Lida",
#         "phone": 380971112255,
#         "email": "lida@gmail.com"
#     }
# }
#
# print(users)
# print(users["Dubinko"]["email"])  # вывод почты из втроеных словарей
# print(users["Marinovkiy"]["phone"]) # вывод телефона из втроеных словарей

