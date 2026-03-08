# Beginner Python Games
# Game 1: Number Guess Game

gusse = 5

num1 = float(input("Gusse a number to play the game(1 - 10): "))

if num1 == gusse:
    print("You Win.")
else:
    print("You Loss")
    if num1 < 5:
        print("your Gusse is low")
    else:
        print("Your Gusse is Heigh \n(choose number lessthen 10)")
