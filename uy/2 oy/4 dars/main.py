# z = ['olma', 'anor', 'docha']
# d = {
#     'olma': 4,
#     'anor': 2,
#     'docha': 3
# }

# iputt = input('Введите название продукта: ')
# if iputt in d:
#     print(d[iputt])

# davlatlar = {
#     'Ozbekiston': 37000000,
#     'Armeniya': 3000000,
#     'Fransia': 68521974
# }

# input_davlat = input('Davlat nomini kiriting:')

# if davlatlar[input_davlat] <= 3000000:
#     print('Веденное вами государство в малой категории')
# elif 3000000 < davlatlar[input_davlat] <= 38000000:
#     print('Веденное вами государство в средней категории')
# elif davlatlar[input_davlat] > 38000000:
#     print('Веденное вами государство в высокой категории')
# else:
#     print('Веденное вами государство ни в какой категрии не состоит')


# poytaxt = {
#     'Ozbekiston':'Toshkent',
#     'Rossia' : 'Moskov',
#     'Fransia' : 'Parij'
# }

# input_poytaxt= input('Davlat nomini kiriting:')
# if input_poytaxt in poytaxt:
#     print(f"Столица страны  {poytaxt[input_poytaxt]}")

# mevalar = {
#     'яблоко': 'красный',
#     'банан': 'желтый',
#     'огурцы': 'зеленый'
# }

# mevalar_input = input('Введите название фрукта: ')
# if mevalar_input in mevalar:
#     color = mevalar[mevalar_input]
#     print(f'Этот фрукт {color}')
# else:
#     print('Этот фрукт неизвестного цвета')


films = {
    "Форрест Гамп": 8.8,
    "Звездные войны": 8.7,
    "Титаник": 7.8,
    "Аватар": 7.8,
    "Интерстеллар": 8.6
}
for film, rating in films.items():
    if rating > 8.5:
        print(f"Фильм {film} имеет высокий рейтинг")
    else:
        print(f"Фильм {film} имеет обычный рейтинг")