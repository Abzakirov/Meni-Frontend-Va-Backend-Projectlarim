# Дни недели
    
kun = int(input("Ведите число от 1 до 7"))    

if kun ==1:
    print("Понидельник")
elif kun == 2:
 print('Вторник')
elif kun == 3:
    print('Среда')
elif kun == 4:
    print('Четверг')
elif kun == 5:
    print('Пятница')
elif kun == 6:
    print('Суббота')
elif kun == 7:
    print('Воскресенье')
else :
    print('Некорректное число')
    
    
    #Oylar
    
month = int(input('Введите номер месяца: '))

if month == 7:
    print('Сейчас летние каникулы')
elif month in [6, 8]:
    print('Сейчас летние каникулы')
else:
    print('Сейчас время для учебы')


    
    #Светофор
    # Попросите пользователя ввести цвет светофора
Kizil = input('Введите цвет светофора: ')

# Дайте команду для каждого цвета отдельно
if Kizil.lower() == 'красный':
    print('Стоп')
elif Kizil.lower() == "жёлтый":
    print('Готовься')
elif Kizil.lower() == "зеленый":
    print('Можете поехать')
else:
    print('Некорректный цвет')

# БУКВЫ
  
harf = input('Введите одну букву: ')

if harf.isupper():
    print('Заглавная буква')
elif harf.islower():
    print('Строчная буква')
else:
    print('Инициалы')

   
    