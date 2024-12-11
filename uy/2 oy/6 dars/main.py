menu = {
    "Стейк": 1000,
    "Паста": 500,
    "Салат": 300,
    "Суп": 200
}


print("Меню ресторана:")
for dish in menu.keys():
    print(dish, "-", menu[dish], "руб.")

print()

dish_choice = input("Введите название блюда из меню: ")

if dish_choice in menu:
    price = menu[dish_choice]
    print("Стоимость блюда", dish_choice, ":", price, "руб.")
    print("Желаете сделать заказ?")
else:
    print("Блюда", dish_choice, "нет в меню.")
    print("Выберите другое блюдо или покиньте ресторан.")
    