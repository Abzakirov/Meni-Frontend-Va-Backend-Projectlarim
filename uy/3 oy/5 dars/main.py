class Personazh:
    def __init__(self, name, level, health, attack):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack

class Voin(Personazh):
    def __init__(self, name, level, health, attack, weapon):
        super().__init__(name, level, health, attack)
        self.weapon = weapon

    def attack(self, target):
        print(f"{self.name} атакует {target} с помощью {self.weapon}!")

class Mag(Personazh):
    def __init__(self, name, level, health, attack, spell):
        super().__init__(name, level, health, attack)
        self.spell = spell

    def use_magic(self, target):
        print(f"{self.name} использует заклинание {self.spell} на {target}!")

class Luchnik(Personazh):
    def __init__(self, name, level, health, attack, bow):
        super().__init__(name, level, health, attack)
        self.bow = bow

    def attack(self, target):
        print(f"{self.name} атакует {target} с помощью {self.bow}!")

voin = Voin("Воин", 1, 100, 10, "меч")
mag = Mag("Маг", 1, 80, 15, "огненный шар")
luchnik = Luchnik("Лучник", 1, 90, 12, "лук")

voin.attack(mag.name)
mag.use_magic(voin.name)
luchnik.attack(voin.name)
