# WAP to enter marks of 3 Subject from the user and store them in a dictinary. start with empty disctinory & one by one. use subject name as key & marks as value.

marks = {}

sub = input("Enter a Subject name:")
mark = float(input("Enter mark of subject:"))
marks.update({sub:mark})

sub = input("Enter a Subject name:")
mark = float(input("Enter mark of subject:"))
marks.update({sub:mark})

sub = input("Enter a Subject name:")
mark = float(input("Enter mark of subject:"))
marks.update({sub:mark})

print(marks)