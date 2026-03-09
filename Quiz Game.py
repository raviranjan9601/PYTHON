# Simple Quiz Game 3 Questions

score  = 0

qustion1 = input("Who's Developed Python?: ").lower()

if qustion1 == "guido van rossum":
    print("Your Answer is Right.")
    score += 1
else:
    print("Your Answer is Wrong.")

qustion2 = input("When Develop Python: ")

if qustion2 == "1991":
    print("Your Answer is Right.")
    score += 1
else:
    print("Your Answer is Wrong.")

qustion3 = input("Python is a Programing Language(yes/no):").lower()

if qustion3 == "yes":
    print("Your Answer is Right.")
    score += 1
else:
    print("Your Answer is Wrong.")

print("Your Score= ",score)

