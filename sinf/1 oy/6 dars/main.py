gender = input("Введите ваш пол: ")
age = int(input("Введите ваш возраст: "))

if gender == 'мужской' and age < 10:
        print("Вы вошли в группу")
elif gender == 'женский' and age > 10:
        print("Вы в группе С")
else:
        print("Вы не того пола")

