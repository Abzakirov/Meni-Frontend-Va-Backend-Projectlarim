class Mushuk:
    def __init__(self, ism, yoshi, rangi):
        self.ism = ism
        self.yoshi = yoshi
        self.rangi = rangi

    def tanishtirmoq(self):
        print(f"Mushukning ismi: {self.ism}, yoshi: {self.yoshi}, paltosining rangi: {self.rangi}")

    def miyov(self):
        print("Miyav!")

mushuk = Mushuk("Tom", 3, "qora")
mushuk.tanishtirmoq()
mushuk.miyov()
