class Kitob:
    def __init__(self, nomi, avtor, jnar):
        self.nomi = nomi
        self.avtor = avtor
        self.jnar = jnar
        self.kopyi = 1

    def olish(self):
        self.kopyi += 1

    def qaytarish(self):
        if self.kopyi > 0:
            self.kopyi -= 1


kitob1 = Kitob('1chi kitob', 'avtor1', 'jnar1')
kitob2 = Kitob('2chi kitob', 'avtor2', 'jnar2')
kitob3 = Kitob('3chi kitob', 'avtor3', 'jnar3')


kitob1.kopyi = 2
kitob2.kopyi = 5
kitob3.kopyi = 4
