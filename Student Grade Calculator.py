# Project 2: Student Grade Calculator

print("Cheak Student Grade")

name = input("Enter Student Name: ")

math = float(input("Enter Math Number: "))
science = float(input("Enter Science Number: "))
hindi = float(input("Enter Hindi Number: "))
english = float(input("Enter English Number: "))
sst = float(input("Enter SST Number: "))

total = math + science + hindi + english + sst

averge = total / 5

print("Student Name: ", name)
print("Total Marks: ", total)
print("Average: ", averge)
print()
print("Thank You :)")






