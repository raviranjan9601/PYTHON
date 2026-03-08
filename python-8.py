# Conditinol Statement

print("Mark Sheet")

name = input("Enter Student Name: ")

math = float(input("Enter Math Mark: "))
science = float(input("Enter Science Mark: "))
sst = float(input("Enter SST Mark: "))
hindi = float(input("Enter Hindi Mark: "))
engilsh = float(input("Enter Engilsh Mark: "))

total = math + science + sst + hindi + engilsh

average = total / 5

print("")
print("Your Total Mark: ", total)
print("")
print("Precentage: ", average)
print("")

print("Your Grade is: ")
if average >= 90:
    print("A+")

elif average >= 70:
    print("A")

elif average >= 65:
    print("B+")

elif average >= 40:
    print("B")

elif average >= 30:
    print("C")

else:
    print("Fail")

