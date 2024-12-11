
student = ['Гурбан', 'ali', 'akbar', 'polat', 'lochin', 'bilol', 'anvar', 'izzatila', 'zohidjon', 'behruz', 'muhammadaziz', 'solihiddin', 'Abdulloh']

name_to_remove = input("ведите имя: ")

if name_to_remove in student:
    student.remove(name_to_remove)

for student in student:
    print(student)
