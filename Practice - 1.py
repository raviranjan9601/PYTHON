# TASK 1:
# --List Input Program--
# Write a program that:
# Takes 5 numbers from the user
# Stores them in a list
# Prints:
# Largest number
# Smallest number
# Sum of numbers
list1 = []

list1.append(int(input("enter a number:")))
list1.append(int(input("enter a number:")))
list1.append(int(input("enter a number:")))
list1.append(int(input("enter a number:")))
list1.append(int(input("enter a number:")))



print(list1)

list1.sort()

print("Largest number of the list : ",list1[-1])
print("Largest number of the list : ",list1[0])
print("Largest number of the list : ", sum(list1))