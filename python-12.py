# write a program to cheak if a list contains a palindrome of element.

palindrome = []

palindrome.append(input("Enter a Number:"))
palindrome.append(input("Enter a Number:"))
palindrome.append(input("Enter a Number:"))
palindrome.append(input("Enter a Number:"))
palindrome.append(input("Enter a Number:"))

palindrome1 = palindrome.copy()

palindrome1.reverse()

if (palindrome == palindrome1):
    print("It is a Palindrome List.")
else:
    print("It is Not a Palindrom list")