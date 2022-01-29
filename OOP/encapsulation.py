# name = input("Введите имя: ")
# age = int(input("Введите возвраст: "))
# print("Привет меня зовут", name, "мне", age, "лет")
# print(f"Привет меня зовут,{name} мне {age} лет")


# class Person:  # создание класса
#     def __init__(self, name): # создание конструктора
#         self.name = name # описание поля
#         self.age = 1  # описание поля
#
#     def display_info(self):   # создание метода
#         print(f"Привет мое имя {self.name}, мне {self.age} лет") # Вывод строк с F-строками
#
#
# person_one = Person(name="Nikitos") # создание обьекта
# person_one.display_info()   # вызов метода
# person_one.name = "Vlad"  # присвоение строки полю
# person_one.age = -10   # присвоение значения полю
# person_one.display_info()  # вызов метода


# class Person:  # создание класса
#     def __init__(self, name):  # создание конструктора с параметром  name
#         self.__name = name  # описание поля со свойством приватности  .__
#         self.__age = 1  # описание поля со свойством приватност .__
#
#     def set_age(self, age):  # создание метода проверкеи возраста
#         if 1 < age < 158:
#             self.__age = age  # при успешном подтверждении поля описуем!
#         else:
#             print("Недопустимый возраст!")
#
#     def get_age(self):   # создание метода возврата  с обращение к age
#         return self.__age
#
#     def get_name(self):  # создание метода возврата  с обращение к name
#         return self.__name
#
#     def display_info(self):   #  создание метода вывода
#         print(f"Привет меня зовут {self.__name}, мне {self.__age} лет!")
#
#
# person_one = Person(name="Nikita")  # создание обьекта класа с присвоением значения name
# person_one.display_info()  # вызов метода
# person_one.set_age(age=-12)  # передача значения age (проверка на возраст так как есть метод проверки)
# person_one.set_age(age=22)  # передача значения age
# person_one.display_info()  # вызов метода


# class Person:  # создание класа
#     def __init__(self, name):  #  создание конструктора с параметрами
#         self.__name = name  #  описание поля
#         self.__age = 1  # описание поля
#
#     @property   #  Обьявление Gettera  ( АНОТАЦИЯ @)
#     def age(self):  # создание метода возврата age
#         return self.__age
#
#     @age.setter  #Обьявление SETTERA ( АНОТАЦИЯ @)
#     def age(self, age):  # создание метода с параметром
#         if 1 < age < 120:
#             self.__age = age  # описание поля
#         else:
#             print("Не верный возраст!")
#
#     @property   # обьявление Gettera
#     def name(self):  # cоздание метода  возврпащения name
#         return self.__name
#
#     def display_info(self):   # создание метода вывоа
#         print(f"Привет меня зовут {self.__name}, мне {self.__age} лет! ")  # Ф строки
#
#
# person_one = Person(name="Nikita")  # создание обьекта с присвоением значение
# person_one.display_info()  # Вызов метода
# person_one.age = -21   # присоение значения
# print(person_one.age)
# person_one.age = 21  # присвоение значение
# person_one.display_info() # вызов метода







