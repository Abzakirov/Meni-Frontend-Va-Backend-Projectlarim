import random

def generate_random_name():
    names = ["Иван", "Алексей", "Максим"]
    femaly_names = ["Анна", "Екатерина", "Мария"]
    gender = random.choice(["male", "female"])
    if gender == "male":
        return random.choice(names)
    else:
        return random.choice(femaly_names)

print(generate_random_name())
    