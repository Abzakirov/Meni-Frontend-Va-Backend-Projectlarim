num = 1

while num<=10:
    print(num,end=", ")

    user = int(input('Ведите число'))
    while user >0:
        print(user)
        user-=1

number = int(input('Введите число: '))
sum_numbers = number * (number + 1) // 2
print("Сумма чисел от 1 до", number, "равна", sum_numbers)


summa = 0
vvod = 1
while vvod != 0:
    vvod = int(input("Введите номер: "))
    summa += vvod
print(summa)

    