class Tovar:
    def __init__(self, nomi, narxi, kolichestvo):
        self.nomi = nomi
        self.narxi = narxi
        self.kolichestvo = kolichestvo

class Electronika(Tovar):
    def __init__(self, nomi, narxi, kolichestvo, garantiya):
        super().__init__(nomi, narxi, kolichestvo)
        self.garantiya = garantiya

class Kiyim(Tovar):
    def __init__(self, nomi, narxi, kolichestvo, razmer):
        super().__init__(nomi, narxi, kolichestvo)
        self.razmer = razmer

class Kitob(Tovar):
    def __init__(self, nomi, narxi, kolichestvo, avtor):
        super().__init__(nomi, narxi, kolichestvo)
        self.avtor = avtor

