# Tuple Inside Dictionary
# Highest marks
# Lowest marks

# tapp = (95, 78, 90)

dict01 = {
    "Name" : "Ravi",
    "Class" : "XII",
    "Mark" : (95, 78, 90)
}

print(dict01)

print(max(dict01["Mark"]))
print(min(dict01["Mark"]))
print((dict01["Mark"]))
# print("mark".min())