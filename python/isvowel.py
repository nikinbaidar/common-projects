def isVowel(char):
    return char in "aeiouAEIOU"

char = input("Enter a character ")

if isVowel(char):
    print("True")
else:
    print("False")
