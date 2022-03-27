#!/usr/bin/env python

def isVowel(char):
  return char in "aeiouAEIOU"

# char = input("Enter a character: ")
char = 'x'

if isVowel(char):
  print("Vowel")
else:
  print("Not vowel")
