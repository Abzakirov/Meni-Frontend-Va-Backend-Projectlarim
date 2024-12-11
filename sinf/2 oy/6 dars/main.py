# epson = {
#     'Anvar':True,
#     'Akbar':False,
#     'Gurban':True,
#     'Izzatilla':False,
#     'Ali':True,
#     'Behruz':False,
#     'Abdulloh':True
# }

# for name, value in epson.items():
#     print(f'{name}: {value}')


# balance = 100
# expenses = []

# while True:
#     print("Выберите пункт:")
#     print("1. Баланс")
#     print("2. Потратить деньги")
#     print("3. Расходы")

#     choice = input("Введите номер пункта: ")

#     if choice == "1":
#         print("Текущий баланс:", balance)
#     elif choice == "2":
#         expense_name = input("Введите название расхода: ")
#         expense_amount = float(input("Введите сумму потраченных денег: "))

#         if expense_amount > balance:
#             print("У вас недостаточно денег!")
#         else:
#             balance -= expense_amount
#             expenses.append(expense_amount)
#             print("Расход успешно добавлен!")
#     elif choice == "3":
#         total_expenses = sum(expenses)
#         print("Список всех расходов:", expenses)
#         print("Общая сумма расходов:", total_expenses)
#         print("Текущий баланс:", balance - total_expenses)
#     else:
#         print("Неверный выбор. Попробуйте снова.")


# user_choose =str('Выберите какое действие хотите выполнить плюс, минус, деление,умножение')
# num1 = int(input('Ведите первое число '))
# num2 = int(input('Ведите второе число '))
# if user_choose == 'плюс':
#     print(num1+num2)
#     if user_choose == 'минус':
#         print(num1/num2)
#     if user_choose == 'деление':
#         print(num1*num2)




weeekdays ={
'Monday' : True,
'Tuesday' : False,
'Wednesday' : True,
'Thursday' : False,
'Friday' : True,
'Saturday' : False,
'Sunday' : True
}

def make_reservation(day):
    if weeekdays.get(day, False):
        print(f"Reservation for {day} is available.")
    else:
        print(f"Reservation for {day} is not available.")


today = "Monday"
make_reservation(today)
    