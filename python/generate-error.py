''' WAP to input a number, if it is not a number then
    generate an error message '''

number = input("Enter a number "); # str
try:
    float(number)
except:
    raise ValueError("Invalid")
else:
    print("Valid")
