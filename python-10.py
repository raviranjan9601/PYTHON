# find the Gratest Value.

num1 = float(input("Enate a Number: "))
num2 = float(input("Ender Second Number: "))
num3 = float(input("Enter third Number: "))

if(num1 > num2 and num1 > num3):
    print("frist Number is Greater", num1)

elif(num2 > num1 and num2 > num3):
    print("second number is grater", num2)

elif(num3 > num2 and num3 > num1):
    print("third number is grater", num3)

else:
    print("Some thing Wrong")

