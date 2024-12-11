# class frukt:
#     def __init__(self, frukt, rangi):
#         self.frukt = frukt
#         self.rangi = rangi


# class meva:
#     def __init__(self, names, color):
#         self.names = names
#         self.color = color

# class olma(meva):
#     def __init__(self, names, color, sort):
#         super().__init__(names, color)
#         self.sort = sort

# class grusha(meva):
#     def __init__(self, names, color, forma):
#         super().__init__(names, color)
#         self.forma = forma

# class apelsin(meva):
#     def __init__(self, names, color, mazasi):
#         super().__init__(names, color)
#         self.mazasi = mazasi

# olma = olma("Красное яблоко", "красный", "Антоновка")
# grusha = grusha("Зеленая груша", "зеленый", "грушевидная")
# apelsin = apelsin("Апельсин", "оранжевый", "сладкий")

# print(olma.names)  
# print(grusha.forma)
# print(apelsin.mazasi)


# class Fruct:
#     def __init__(self, nomis, rangis):
#         self.nomis = nomis
#         self.rangis = rangis

# class Apple(Fruct):
#     def __init__(self, nomis, rangis, sorti):
#         super().__init__(nomis, rangis)
#         self.sorti = sorti

#     def eish(self):
#         print(f"Съедено яблоко {self.nomis}")

#     def tekshirish(self):
#         print(f"Проверка свежести яблока {self.nomis}")

# class Grush(Fruct):
#     def __init__(self, nomis, rangis, forma):
#         super().__init__(nomis, rangis)
#         self.forma = forma

#     def eish(self):
#         print(f"Съедена груша {self.nomis}")

#     def tekshirish(self):
#         print(f"Проверка свежести груши {self.nomis}")

# class Orange(Fruct):
#     def __init__(self, nomis, rangis, tami):
#         super().__init__(nomis, rangis)
#         self.tami = tami

#     def eish(self):
#         print(f"Съеден апельсин {self.nomis}")

#     def tekshirish(self):
#         print(f"Проверка свежести апельсина {self.nomis}")

# apple = Apple("Красное яблоко", "красный", "Антоновка")
# grush = Grush("Зеленая груша", "зеленый", "грушевидная")
# orange = Orange("Апельсин", "оранжевый", "сладкий")

# grush.eish()  
# grush.tekshirish()  
# orange.eish()  


class mevalar:
    def __init__(self, ismi, colors):
        self.ismi = ismi
        self.colors = colors

    def rangini_korish(self):
        print(f"Цвет фрукта {self.ismi}: {self.colors}")

    def iesh(self):
        print(f"Съеден фрукт {self.ismi}")

    def svejost_tekshirih(self):
        print(f"Проверка свежести фрукта {self.ismi}")

olmalar = mevalar("Яблоко", "красный")
grushalar = mevalar("Груша", "зеленый")
apelsinlar = mevalar("Апельсин", "оранжевый")

vbor = input("Выберите фрукт (яблоко, груша, апельсин): ")

if vbor == "яблоко":
    olmalar.rangini_korish()
    olmalar.iesh()
    olmalar.svejost_tekshirih()
elif vbor == "груша":
    grushalar.rangini_korish()
    grushalar.iesh()
    grushalar.svejost_tekshirih()
elif vbor == "апельсин":
    apelsinlar.rangini_korish()
    apelsinlar.iesh()
    apelsinlar.svejost_tekshirih()
else:
    print("Некорректный выбор фрукта")
