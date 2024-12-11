def create_friends_dict():
    friends_dict = {}
    while True:
        friend_name = input("Do'stingizning ismini kiriting (yoki to'xtatish uchun 'stop' deb yozing): ")
        if friend_name.lower() == 'stop':
            break
        friend_age = input("Do'stingizning yoshini kiriting: ")
        friends_dict[friend_name] = int(friend_age)
    return friends_dict

dostlar = create_friends_dict()
print(dostlar)

def sum_numbers_in_list():
    sonlar = input("Raqamlarni probel orqali kiriting: ").split()
    sonlar = list(map(int, sonlar))
    return sum(sonlar)

natija = sum_numbers_in_list()
print("Ro'yxatdagi barcha raqamlar yig'indisi:", natija)

def remove_duplicates():
    royxat = input("Ro'yxatni probel orqali kiriting: ").split()
    noyob_elementlar = list(set(royxat))
    return noyob_elementlar

yangi_royxat = remove_duplicates()
print("Dublikatlardan tashqari ro'yxat:", yangi_royxat)
