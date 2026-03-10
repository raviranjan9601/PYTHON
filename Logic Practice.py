# Even & Odd Finder
# User enters numbers into a list.
# Your program should print:
numbers = list(map(int, input("Enter 5 numbers: ").split()))
numbers = list(int(input("Enter 5 numbers: ").split()))

even = []
odd = []

if numbers[0] % 2 == 0:
    even.append(numbers[0])
else:
    odd.append(numbers[0])

if numbers[1] % 2 == 0:
    even.append(numbers[1])
else:
    odd.append(numbers[1])

if numbers[2] % 2 == 0:
    even.append(numbers[2])
else:
    odd.append(numbers[2])

if numbers[3] % 2 == 0:
    even.append(numbers[3])
else:
    odd.append(numbers[3])

if numbers[4] % 2 == 0:
    even.append(numbers[4])
else:
    odd.append(numbers[4])

print("Even numbers:", even)
print("Odd numbers:", odd)