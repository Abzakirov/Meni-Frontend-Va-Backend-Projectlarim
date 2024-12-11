# hello = 0
# while True:
#     hello +=1
#     print(hello)






n = int(input("Введите число: "))
sum = 0
current_number = 1

while current_number <= n:
    sum += current_number
    current_number += 1

print("Сумма чисел до", n, "равна", sum)
