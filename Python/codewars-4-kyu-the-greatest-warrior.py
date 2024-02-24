class Warrior():

    def __init__(self):
        self.RANKS = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
        self.level = 1
        self.rank = self.RANKS[0]
        self.experience = 100
        self.achievements = []

    def level_up(self, exp_points):
            self.experience += exp_points
            if self.experience > 10000:
                self.experience = 10000
            self.level = int(self.experience/100)
            self.rank = self.RANKS[int(self.level/10)]

    def training(self, arr):
        description = arr[0]
        exp_points = arr[1]
        min_level = arr[2]
        if self.level >= min_level:
            self.level_up(exp_points)
            self.achievements.append(description)
            return description
        return "Not strong enough"
    
    def battle(self, enemy_level):
        if (enemy_level < 0) or (enemy_level > 100):
            return "Invalid level"
        elif enemy_level == self.level:
            self.level_up(10)
            return "A good fight"
        elif self.level - enemy_level == 1:
            self.level_up(5)
            return "A good fight"
        elif self.level - enemy_level > 1:
            return "Easy fight"
        elif (int(enemy_level/10) > int(self.level/10)) and (enemy_level - self.level) >= 5:
            return "You've been defeated"
        elif enemy_level > self.level:
            diff = enemy_level - self.level
            self.level_up(20*diff*diff)
            return "An intense fight"


        
