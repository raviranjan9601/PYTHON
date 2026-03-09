# Game 2: Yes / No Game

print("---its Game Time---")

answer = input("Do You Like Python? (Yes/No): ").capitalize()

if answer == "Yes":
    print("Great! ")
elif answer == "No":
    print("Give it Some Time, You Love it.")
else:
    print("Invalid Answer :(")