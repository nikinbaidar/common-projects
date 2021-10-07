
############################################################################
# This program returns an array that is the square of every element in the #
# array named "listOfIntegers".                                            #
############################################################################

def square(array):
    return [element**2 for element in array]

listOfIntegers = [6250,7500,5600,6900,5150,6800,6300,5000,8000,5500,5200,5500]
result = square(listOfIntegers)
print(result)
print(len(listOfIntegers))


