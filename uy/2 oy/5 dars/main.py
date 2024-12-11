# frukt = {
#     'olma':5,
#     'banan':4,
#     'giloz':3,
#     'ananas':6,
# }

# frukt_names = list(frukt.keys())
# frukt_name = list(frukt.values())
# print(frukt_names)
# print(frukt_name)


# countries = {
#     "Узбекистан": "Ташкент",
#     "Франция": "Париж",
#     "Германия": "Берлин",
#     "Италия": "Рим"
# }
# country =list(countries.items())
# print(country)


# cities = {
#     "Ташкент": "2 млн",
#     "Париж": "2.1 млн",
#     "Москва": "12 млн",
#     "Лондон": "8 млн"
# }

# cities_input =  input('Qaysi shaxarni ochirmoxchisiz')
# cities_result = cities.pop(cities_input)
# print(cities_result)
# print(cities)


# population = {
#     "Россия": "144 млн",
#     "Франция": "67 млн",
#     "Германия": "83 млн",
#     "Италия": "60 млн"
# }


# print('Davlatlar nomi:')

# for countys in population.keys():
#     print(countys)

# print('Aholi:')

# for countys in population.values():
#     print(countys)

# print("Пары 'название страны-население':")
# for country, population_count in population.items():
#     print(country, "-", population_count)

# total_population = sum(int(population_count.split()[0]) for population_count in population.values())
# print('Общее население стран',total_population)


# films = {
#     "Форрест Гамп": 8.8,
#     "Звездные войны": 8.7,
#     "Титаник": 7.8,
#     "Аватар": 7.8
# }


# while films:
#     print("Список фильмов:", list(films.keys()))
#     film = input("Введите название фильма, который вы хотите удалить: ")

#     if film in films:
#         films.pop(film)
#         print("Фильм", film, "был удален из словаря.")
#     else:
#         print("Фильм", film, "не найден в словаре.")

# print("Словарь пуст.")



