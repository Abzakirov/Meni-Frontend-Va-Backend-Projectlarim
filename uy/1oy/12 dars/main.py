import random

topilgan_raqam = random.randint(1,10)
urinishlar = 0

while True :
    kiritilgan_raqam = int(input('Ведите число от 1 до 10'))
    urinishlar +=1
    if kiritilgan_raqam < topilgan_raqam:
        print('Ваше число маленькое ')
    elif kiritilgan_raqam > topilgan_raqam:
        print('Ваше число большое')
    else:
        print('Поздравляю вы угадали число за',urinishlar,'попытки ')
        break

password = 'something'
while True :
 int_password = input('Ведите пароль ')
 if int_password == password:
   print('Пароль веден правильно')
   break
else:
   print('Попробуйте ещё раз пароль веден неправильно')
 