class football_player:
    def __init__(self, age_football, ismi, familiya, height):
        self.age_football = age_football
        self.ismi = ismi
        self.familiya = familiya
        self.height = height

    def football_info(self):
        return f'({self.age_football} ismi - {self.ismi} faliyasi - {self.familiya} boyi - {self.height})'

obj1 = football_player(39, 'ronaldo', 'birnarsa', 175)  # object
print(obj1.football_info())
