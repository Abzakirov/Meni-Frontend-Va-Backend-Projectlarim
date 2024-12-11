class Talaba:
    def __init__(self, ismi, yoshi, fanlar):
        self.ismi = ismi
        self.yoshi = yoshi
        self.fanlar = fanlar

class FanniOqitish:
    def __init__(self, nomi, daraja):
        self.nomi = nomi
        self.daraja = daraja

class Oquvchi:
    def __init__(self, ismi, yoshi):
        self.ismi = ismi
        self.yoshi = yoshi
        self.obyektlar = []

    def add_fan(self, fan):
        self.obyektlar.append(fan)

matematika = FanniOqitish("Matematika", "Oliy")
tarix = FanniOqitish("Tarix", "O'rta")
adabiyot = FanniOqitish("Adabiyot", "O'rta")


talaba1 = Oquvchi("Ali", 15)
talaba1.add_fan(matematika)
talaba1.add_fan(tarix)

talaba2 = Oquvchi("Vali", 16)
talaba2.add_fan(adabiyot)
talaba2.add_fan(tarix)


print(talaba1.ismi, talaba1.yoshi, [fan.nomi for fan in talaba1.obyektlar])
print(talaba2.ismi, talaba2.yoshi, [fan.nomi for fan in talaba2.obyektlar])
