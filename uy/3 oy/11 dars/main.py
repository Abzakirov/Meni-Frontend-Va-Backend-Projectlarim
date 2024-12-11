class Mijoz:
    def __init__(self, ism, balans):
        self.ism = ism
        self.balans = balans

    def show_account(self):
        print(f"Mijoz: {self.ism}")
        print(f"Balans: {self.balans}")


class Bank:
    def __init__(self):
        self.mijozlar = []

    def add_customer(self, mijoz):
        self.mijozlar.append(mijoz)

    def mijozni_topish(self, ism):
        for mijoz in self.mijozlar:
            if mijoz.ism == ism:
                return mijoz
        return None


bank = Bank()

mijoz1 = Mijoz("Ali", 1000)
mijoz2 = Mijoz("Vali", 500)
mijoz3 = Mijoz("Hasan", 2000)

bank.add_customer(mijoz1)
bank.add_customer(mijoz2)
bank.add_customer(mijoz3)

for mijoz in bank.mijozlar:
    mijoz.show_account()

mijoz = bank.mijozni_topish("Ali")
if mijoz:
    mijoz.balans += 500
    mijoz.show_account()
else:
    print("Mijoz topilmadi.")
