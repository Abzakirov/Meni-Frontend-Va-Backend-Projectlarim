class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    def move(self):
        print("Автомобиль движется.")

    def stop(self):
        print("Автомобиль остановился.")

    def change_speed(self, new_speed):
        self.speed = new_speed

    def information(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year}, Цвет: {self.color}, Текущая скорость: {self.speed}")

car = Car("Audi", "A4", 2019, "черный")
car.move()
car.stop()
car.change_speed(60)
car.information()
