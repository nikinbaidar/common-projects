from os import system

system("clear")

string_1 = "foo"
string_2 = "bar"

print("AND operator demonstration",end="\n\n")

print(not True and True)
print((not True) and True)
print(not (True and True)) ; print()

print(not False and True)
print((not False) and True)
print(not (False and True)) ; print()

print(not True and False)
print((not True) and False)
print(not (True and False)) ; print()

print(not False and False)
print((not False) and False)
print(not (False and False)) ; print()

print("OR Operator demonstration",end="\n\n")

print(not True or True)
print((not True) or True)
print(not (True or True)) ; print()

print(not False or True)
print((not False) or True)
print(not (False or True)) ; print()

print(not True or False)
print((not True) or False)
print(not (True or False)) ; print()

print(not False or False)
print((not False) or False)
print(not (False or False)) ; print()
