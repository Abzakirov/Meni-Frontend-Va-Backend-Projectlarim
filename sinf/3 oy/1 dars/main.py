class Employee(Person):
    def __init__(self, familiya, t_yili, jinsi, mashinalari, t_shahar, lavozim):
        super().__init__(familiya, t_yili, jinsi, mashinalari, t_shahar)
        self.lavozim = lavozim

    def malumotlar(self):
        return f"{super().malumotlar()} Lavozimi: {self.lavozim}"

    def mashinalarini_korish(self):
        return f"{self.familiya}ning mashinalari: {', '.join(self.mashinalari)}"

obj2 = Employee('Zohidov', 2008, 'erkak', ['merc', 'bmw'], 'toshkent', 'mudir')
print(obj2.malumotlar())
print(obj2.mashinalarini_korish())
