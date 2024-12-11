# Savollar

# 1-savol: print() bu...

# #Javob:
# print исвользуеттся для вывода текста значений на экран.Он ползволяет узнать информацию пользователя или отложенные сообщения во время выполнения программы

# Kod namunasi:
print('SAlom')
# 2-savol: input() bu...
# #Javob:
# input используется для ввода данных от пользователя и он позволяет программировать ожидаеммый ввод данных от пользоваиеля и сохранять их в переменные

# Kod namunasi:
ism = input('Как вас звать ')
print('Привет',ism)
# 3-savol: O'zgaruvchi nima?

# #Javob:
# Переменная это хранилище для данных которое позволяет сохранять значения,в различных частях кода
# Kod namunasi:
x = 5
y = 4
print(x+y)
# 4-savol: 4 ta maʼlumot turini sanab oʻting va misol keltiring:

# #Javob:
# 1 Числа (цифры): Включает целые числа (целые числа) и числа с плавающей точкой (плавающие числа).
# 2 Строки (Струны): состоят из символов, заключенных в кавычки.  
# 3 Списки (списки): представляют собой упорядоченные элементы коллекции
# 4 Булевы значения (логические значения): можно принять только два значения — True (истина) или False (ложь). 
# Kod namunasi:
#1
x = 5
y = 3.14
# 2
name = "John"
message = 'Привет, мир!'
# 3 
numbers = [1, 2, 3, 4, 5]
fruits = ["яблоко", "банан", "апельсин"]
#4
is_true = True
is_false = False


# 5-savol: String formatlash nima va Pythonda ikkita formatlash usuliga misol keltiring:

# #Javob:
# Метод format(): Этот метод позволяет задавать значения значений в тексте, используя заливку в фигурных скобках.
# Kod namunasi:
name = "John"
age = 25
message = "Меня зовут {}, и мне {} лет.".format(name, age)
print(message)

# 6-savol: If, elif, else for nima va ular bilan misol ko'ring:


# #Javob:
# это ключевые слова используемые для создания условных выражений
# Kod namunasi:
x = 10

if x > 10:
    print("x больше 10")
elif x < 10:
    print("x меньше 10")
else:
    print("x равно 10")

# 7-savol: Taqqoslash operatorlarini sanab bering va ularga misol keltiring:

# #Javob:
 # 1 Оператор равенства ( ==): Сравнивает два значения равенства
 # 2 Оператор символа ( !=): Сравнивает два значения символа
 # 3 Оператор больше ( >): Доказывает, что одно значение больше другого. 
 # 4 Оператор меньше ( <): Доказывает, что одно значение меньше другого
# Kod namunasi:
# 1
x = 5
y = 10
print(x == y)  # False
# 2
x = 5
y = 10
print(x != y)  # True
# 3
x = 5
y = 10
print(x > y)  # False
#4
x = 5
y = 10
print(x < y)

# 8-savol: Mantiqiy operatorlar va, yo'q yoki qanday qilib ular bilan misol keltiring:

# #Javob:
# Логические операторы в Python позволяют комбинировать условия и выполнять над ними логические операции
# Kod namunasi:
x = 5
y = 10

# Пример с оператором "и" (and)
if x > 0 and y > 0:
    print("Оба числа положительные")

# Пример с оператором "а не" (not)
if not x == y:
    print("Числа не равны")

# 9-savol: Loop nima va while sikli qanday ishlaydi:

# #Javob:
# Цикл в программировании - это конструкция, которая позволяет выполнять повторяющиеся действия до тех пор, пока прогресс не достигнет состояния. Цикл while— один из видов циклов в Python. Цикл while работает до тех пор пока не достигнет своей цели 
# После выполнения блока кода внутри цикла программа возвращается к началу цикла и снова к следующему условию. Если условие по-прежнему истинно, цикл повторяется. Если условие ложно, выполнение цикла прекращается.


# Kod namunasi:
count = 0
while count < 5:
    print("Текущее значение count:", count)
    count += 1

# 10-savol: For va while o'rtasidagi farq nima va misol keltiring:

# #Javob:
# Цикл for используется, когда заранее известно количество итераций, которые необходимо выполнить. Он состоит из трех частей: создания, условий и обновлений.
# Цикл while используется, когда количество итераций известно заранее и зависит от условий. Он продолжает выполняться до тех пор, пока условие истинно
# Kod namunasi:
for i in range(5):
    print(i)


count = 0
while count < 5:
    print(count)
    count += 1

# 11-chi: Endi siz o'yin qilishingiz kerak: tosh, qog'oz, qaychi.

# Ya'ni, bu o'yinni ikkita o'yinchi o'ynashiga ishonch hosil qilishingiz kerak, omad tilaymiz!

player1 = input("Игрок 1, выберите камень (r), ножницы (s) или бумагу (p): ")
player2 = input("Игрок 2, выберите камень (r), ножницы (s) или бумагу (p): ")

if player1 == player2:
    print("Ничья!")
elif (player1 == "r" and player2 == "s") or (player1 == "s" and player2 == "p") or (player1 == "p" and player2 == "r"):
    print("Игрок 1 победил!")
else:
    print("Игрок 2 победил!")
