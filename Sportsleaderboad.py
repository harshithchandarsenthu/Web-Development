class Team:
    def __init__(self, score):
        self.__score = 0
        self.set_score(score)
    def set_score(self, score):
        if isinstance(score, int) and score >= 0:
            self.__score = score
        else:
            print("Invalid score!")
    def get_score(self):
        return self.__score
    def display_score(self):
        print("Score:", self.__score)
class Hull(Team):
    def display_score(self):
        print("Hull City Score:", self.get_score())
class MUN(Team):
    def display_score(self):
        print("Manchester United Score:", self.get_score())
class Liverpool(Team):
    def display_score(self):
        print("Liverpool Score:", self.get_score())
sports = [Hull(1), MUN(4), Liverpool(2)]
for sport in sports:
    sport.display_score()
Hull, MUN = sports[0], sports[1]
MUN.__score = 3 # Private data can't be accesed from outside the data.
print(Hull.get_score())
for value in [2, 2, -1]:
    MUN.set_score(value)
print("Final Score:", Hull.get_score())
Team(-9).display_score