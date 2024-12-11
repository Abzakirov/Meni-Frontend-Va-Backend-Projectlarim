def chek(word):
    return word == word[::-1]
input_word= input("Ведите слово")
result = chek(input_word)
print(result)

username = 'abdullazokirov808'
password = '20080806'

input_username = input('Ведите почту:')
input_password = input('Ведите пароль:')
 
if input_username  == username and input_password==password:
    print('Добро пожаловать!')
else:
    print('Пока')


num1 = int(input('Введите чётное число: '))

if num1 % 2 == 0:
    print('Четное число')
else:
    print('Нечетное число')


    