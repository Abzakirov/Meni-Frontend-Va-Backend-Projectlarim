# class Magaz:
#     def __init__(self, nomi, adres):
#         self.nomi = nomi
#         self.adres = adres
#         self.tovar = {}

#     def tovarqoshish(self, nomi, stoimost):
#         self.tovar[nomi] = stoimost

#     def tovaruchirish(self, nomi):
#         if nomi in self.tovar:
#             del self.tovar[nomi]

class magazin:
    def __init__(self, name, adres):
        self.name = name
        self.adres = adres
        self.tovars = {}

    def tovar_qoshish(self, name, narxi):
        self.tovars[name] = narxi

    def tovar_uchirish(self, name):
        if name in self.tovars:
            del self.tovars[name]

    def tovar_sotish(self, name, qolichestvo):
        if name in self.tovars and self.tovars[name] >= qolichestvo:
            narxi = self.tovars[name] * qolichestvo
            self.tovars[name] -= qolichestvo
            return narxi
        else:
            return 0
