class Person:  # создание класа
    def __init__(self, name):  # создание конструктора
        self.name = name  # Описание поля

    def display(self):  # создание метода
        print("Примет меня зовут", self.name)  # вывод с обращением к полю или атрибуту


class Auto:  # создание класса
    def __init__(self, brand):  # созадние конструктора
        self.brand = brand  # описание поля

    def move(self, speed):  # создание метода
        print(self.brand, "едет со скоростью", speed, "км/ч") # вывод с обращением к полю бренд и атр


