balanse = 20000
while True:
    air = 2000
    tf = 3000
    bk = 155
    mc = 15000
    input_raqam = int(input('Введите число: '))
    if input_raqam == 1:
        print(balanse)
    elif input_raqam == 2:
        print(air)
        javob = input('Вы точно хотите купить этот товар? (да или нет): ')
        if javob == 'да':
            balanse -= air

        elif input_raqam == 3:
            print(tf)
            javob = input('Вы точно хотите купить этот товар? (да или нет): ')
        if javob == 'да':
            balanse -= tf
        elif input_raqam == 4:
            print(bk)
            javob = input('Вы точно хотите купить этот товар? (да или нет): ')
        if javob == 'да':
            balanse -= bk
        elif input_raqam == 5:
            print(mc)
            javob = input('Вы точно хотите купить этот товар? (да или нет): ')
        if javob == 'да':
            balanse -= mc
            break



print('1.Balanse,\n ','2.Airpods \n','3.telefon \n','4.book \n','5.mackbook')