# Convert to Cases

Name = input("Enter Your Name: ")

print("Choose Witch Case print Your name.\n 1.) UpperCase. \n 2.) LowerCase.")

case1 = input("Enter Your Case: ")

if case1 == "Uppercase" or case1 == "1" or case1 == "uppercase":
    print(Name.upper())

elif case1 == "Lowercase" or case1 == "2" or case1 == "lowercase":
    print(Name.lower())    



