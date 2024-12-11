def yosh(age):
    if age <= 4 or age >= 65:
        return 'Бесплатно'
    elif 5 <= age <= 12:
        return 'Цена билета 15000 сум'
    else:
        return 'Цена билета 20000 сум'

user_age = int(input("Пожалуйста, введите ваш возраст: "))
price = yosh(user_age)
print(price)


def havo (temp):
    if temp <= 0:
        return 'Слишком холодно'
    elif temp >= 30:
        return 'Слишком жарко'
    else :
        return "Температура очень комфорная"
    
        
user_temp = float(input('Пожалуйста ведите температуру воздуха'))
temp_user = havo(user_temp)
print(temp_user)    



def baxo(baho):
    if baho >= 90:
        return 'Отлично'
    elif 80 <= baho < 90:
        return "Хорошо"
    else:
        return "Плохо"

user_baxo = int(input('Введите балл учащегося: '))
user_baho = baxo(user_baxo) 
print(user_baho)
