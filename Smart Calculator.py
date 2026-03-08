# Mini Projects (Day 1 Level)
# Project 1: Smart Calculator

print("SIMPLE CALCULATER")

num1 = float(input("Enter a Number: "))
num2 = float(input("Enter a Number: "))

print("Choose Operation")
# print("type '1' if you ADD")
# print("type '2' if you Subtract")
# print("type '3' if you Multiply")
# print("type '4' if you Divide")

# choice = input("Choose one '1, 2, 3, 4': ")

# if choice == "1":
#     print("Result:", num1 + num2)

# elif choice == "2":
#     print("Result: ", num1 - num2)

# elif choice == "3":
#     print("Result: ", num1 * num2)

# elif choice == "4":
#     print("Result: ", num1 // num2)

# else:
#     print("Invalid Choice")

chose = input("choose one: '+', '-', '*', or '/': ")

if chose == "+":
    print("Result: ", num1 + num2)
    
elif chose == "-":
    print("Result: ", num1 - num2)

elif chose == "*":
    print("Result: ", num1 * num2)

elif chose == "/":
    print("Result: ", num1 // num2)

else:
    print("invalid Choice.")
