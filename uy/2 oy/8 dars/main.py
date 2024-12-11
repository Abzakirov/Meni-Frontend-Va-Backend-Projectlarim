# def say_hello(name):
#     print("Привет, " + name + "!")


# say_hello("Анна")
# say_hello("Петр")
# say_hello("Мария")

def calculate_sum(*args):
    return sum(args)

result1 = calculate_sum(5, 3)
result2 = calculate_sum(10, -2)
result3 = calculate_sum(2.5, 1.5)
result4 = calculate_sum(1, 23, 4, 5, 6)

print("Sum result:", result1)
print("Sum result:", result2)
print("Sum result:", result3)
print("Sum result:", result4)


# def print_list_numbers(numbers):
#     for number in numbers:
#         print(number)

# list1 = [1, 2, 3, 4, 5]
# list2 = [10, 20, 30, 40, 50]
# list3 = [100, 200, 300, 400, 500]

# print("Элементы списка:")
# print_list_numbers(list1)

# print("Элементы списка:")
# print_list_numbers(list2)

# print("Элементы списка:")
# print_list_numbers(list3)


# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False

# result1 = is_even(4)
# result2 = is_even(7)
# result3 = is_even(0)

# print("Результат проверки на четность:", result1)
# print("Результат проверки на четность:", result2)
# print("Результат проверки на четность:", result3)


# def print_numbers(start, end):
#     for number in range(start, end + 1):
#         print(number)


# print("Числа от 1 до 5:")
# print_numbers(1, 5)

# print("Числа от 10 до 15:")
# print_numbers(10, 15)

# print("Числа от -3 до 3:")
# print_numbers(-3, 3)
