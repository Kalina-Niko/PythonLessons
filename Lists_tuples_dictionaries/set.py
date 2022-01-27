# users = {"Alina", "Ivan", "Galina", "Alina"} # Создание сета
# print(users)

# car = ["Mersedes", "BMW", "BMW", "Fiat"]
# print(car)
# car_finally = set(car) # конвертация листов в сеты
# print(car_finally)

# a = set() # Ввод пустого сета
# print(a)

# users = {"Jora", "Jasha", "Siviy", "Jaga", "Jora"}
# print(len(users))  # Вывод длины с учетом уникальных значений

# user = set()
# user.add("Jorik") # Добавление значения в сет
# print(user)

# users = set()
#
# while True:
#     user_input = input("Введите Имя юзера: ")
#     users.add(user_input)   # добавление значения в сет в цикле, от пользователя!
#     if user_input == "хватит":  # если добавление строка хватит тогда цикл останавливается!
#         break
#
# print(users)


# users = {"Alina", "Ivan", "Galina", "Alina"}
# name_pidora = input("Введите имя пользователя которого хотите удалить: ")
#
# if name_pidora in users:
#     users.remove(name_pidora) # Удаление значение в случае если оно есть в Юзерс!
# else:
#     print("Пидора не найдено")
#
# print(users)
# print("Имя пидора", name_pidora)

# users = {"Alina", "Ivan", "Galina", "Alina"}
# name_pidora = input("Введите имя пользователя которого хотите удалить: ")
#
# users.discard(name_pidora)  # Удаление значения из сета!
# print(users)
# print(users.discard(name_pidora))
#
# users.clear()  # Полная очистка сета!
# print(users)

# city = {"Kyiv", "Krivii Rih", "Rovno", "Odesa"}
#
# for i in city:    # Прогон сета циклом фор!
#     print(i)

# city = {"Kyiv", "Krivii Rih", "Rovno", "Odesa"}
# city_too = city.copy()  # Копирование из сета сити в сет сити_ту
# print(city_too)
# print(city)

# users = {"Alina", "Ivan", "Galina", "Alina"}
# users_2 = {"Jora", "Jasha", "Siviy", "Jaga", "Jora"}
# users_3 = users.union(users_2) # Обьединия сетов!
# print(users_3)


# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
# users_3 = users.intersection(users2) # Удаление из сета юзерс в случае если в юзерс два есть Дубли или повт. знач!
# print(users_3)


# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
# users_3 = users.difference(users2) # Вывод всего сета юзерс без дубля из другого сета (юзерс2)
# print(users_3)


