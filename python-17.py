# Student Dictionary

_name = input("Enter Student Name: ")
_age = int(input("Enter Student Age: "))
_mark = float(input("Enter Total Marks: "))

student_data = {}

student_data.update({"name" : _name})
student_data.update({"age" : _age})
student_data.update({"mark" : _mark})

print(student_data)
print("student name:",student_data["name"])
print("Student Age:",student_data["age"])
print("Student Mark:",student_data["mark"])