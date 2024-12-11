print('Добро пожаловать', 'Наше расписание') 
 
Zeitplan = { 
    'Понедельник': 'Занято', 
    'Вторник': 'Занято', 
    'Среда': 'Свободно', 
    'Четверг': 'Свободно', 
    'Пятница': 'Занято', 
    'Суббота': 'Занято', 
    'Воскресенье': 'Занято' 
} 
 
day = int(input('Введите число от 1 до 7: ')) 
 
while True: 
    if day == 1: 
        if Zeitplan['Понедельник'] == 'Занято': 
            print('Мест нет') 
        else: 
            print('Можно записаться') 
        break 
    elif day == 2: 
        if Zeitplan['Вторник'] == 'Занято': 
            print('Мест нет') 
        else: 
            print('Можно записаться') 
        break 
    elif day == 3: 
        if Zeitplan['Среда'] == 'Занято': 
            print('Мест нет') 
        else: 
            print('Можно записаться') 
        break 
    elif day == 4: 
        if Zeitplan['Четверг'] == 'Занято': 
            print('Мест нет') 
        else: 
            print('Можно записаться') 
        break 
    elif day == 5: 
        if Zeitplan['Пятница'] == 'Занято': 
            print('Мест нет') 
        else: 
            print('Можно записаться') 
        break 
    elif day == 6: 
        if Zeitplan['Суббота'] == 'Занято': 
            print('Мест нет') 
        else: 
            print('Можно записаться') 
        break 
    elif day == 7: 
        if Zeitplan['Воскресенье'] == 'Занято': 
            print('Мест нет') 
        else: 
            print('Можно записаться') 
        break 
    else: 
        print('Некорректный ввод. Введите число от 1 до 7.') 
        day = int(input('Введите число от 1 до 7: '))