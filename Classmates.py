classmates = ["Mithun", "Abishek", "Aravind", "Adrian", "Simeon"]
print("Original list:", classmates)
print("First classmate:", classmates[0])
print("Third classmate:", classmates[2])
classmates.append("Sai")
print("After adding a name:", classmates)
classmates.remove("Abishek")
print("After removing a name:", classmates)
classmates.sort()
print("Sorted list:", classmates)
classmates.reverse()
print("Reversed list:", classmates)
teacher = {"name": "Mrs. Rajeshwari", "subject": "Mathematics","experience": 10}
print("\nTeacher's profile:", teacher)
print("Teacher's name:", teacher["name"])
print("Subject:", teacher["subject"])
teacher["subject"] = "English"
teacher["experience"] = 12
print("Updated teacher's profile:", teacher)
student_names = ["Mithun", "Aravind", "Adrian", "Simeon"]
roll_numbers = [1, 2, 3, 4]
student_directory = dict(zip(student_names, roll_numbers))
print("\nStudent directory:", student_directory)
