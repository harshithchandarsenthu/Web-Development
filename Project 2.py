class Student:
    grade = 9
    name = "Harshith"
    def sentence(self):
        print("I am a student who studies in a school.")
    def display(self):
        print(self.grade, self.name)
s1 = Student()
s1.sentence()
s1.display()