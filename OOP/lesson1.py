# class Person: # создание класса
#     name = "Nikita" # атрибут
#     age = 29  # атрибут
#
#     def display_info(self):  # создание метода класса
#         print("Меня зовут", self.name, "мне", self.age, "лет!")  # Вывод с обращениями к атрибутам
#
#     def print_age(self):  # создание метода класса
#         print("Ска мне уже", self.age) # вывод с обращением к атрибуту
#
#
# person_one = Person()  # создание объекта класса
# person_one.display_info()  # запуск метода класса
# person_one.print_age()  # запуск метода класса

# n = input("Как Вас зовут: ")
# a = int(input("Сколько Вам лет: "))
#
#
# class Person:   # создание класса
#     def __init__(self, name, age):  # создание конструктора с параметрами
#         self.name = name  # описание полей
#         self.age = age   # описание полей
#
#     def display(self):   # создание метода с параметром обращения
#         print("Привет меня зовут", self.name, "мне", self.age, "лет!") # вывод с обращениями к полям
#
#
# person_one = Person(name=n, age=a)  # создание объекта класа с параметрами к которые инпуты от пользователя
# person_one.display() # вызов метода
#
# person_two = Person(name="Valentin", age=67) #  создание второго объекта с параметрами которые вносяться
# person_two.display()  # вызов метода

# class Person:  # создание класса
#     def __init__(self, name): # создание конструктора
#         self.name = name # описание поля
#
#     def __del__(self): # создание диструктора
#         print(self.name, "удален из памяти!") # вывод удаленного диструктором поля(атрибута)
#
#     def display(self):  # создание метода
#         print("Привет меня зовут", self.name) # вывод с обращением к полю(атрибуту)
#
#
# person_one = Person(name="Nikitos") # создание объекта с параметром которое вноситься
# person_one.display() # вызов метода
# del person_one  # вызов диструктора оператором del
# person_two = Person(name="Valentin") # создание второго объекта с параметром которое вноситься
# person_two.display() # вызов метода



