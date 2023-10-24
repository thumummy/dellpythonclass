# a program to check temperature
temperature = 65

if temperature > 37:
    print("it is too hot")
else:
    print("it is cold")

# a python program that checks 3 numbers and display the largest number
num1 = 67
num2 = 24
num3 = 6

if num1 > num2 and num1>num3 :
    print(num1 , "is the largest number")
elif num2 > num1 and num2 > num3 :
    print(num2 , "is the largest number")
else:
    print(num3 , "is the largest number")

# a python program tthat checks if a numbe is odd or even
number = 37
if number % 2 == 0:
    print(number , "is an even number")
else :
    print(number , "is an odd number ")


# assignment1 a program that checks whether a year is a leap year or not
year = 2023

if year % 4 == 0:
    print(year ,"is a leap year")
else:
    print(year , "is not a leap year")



# assignment2 check whether an alphabet letter is a consonant or a vowel.
# Python program to check whether the given character
# is a vowel or consonant

# Get an input character from the user
character = input("Enter a character: ")

# Creating a list of vowels
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# Check if the character is a vowel or not
if character in vowels:
    print(f"The character '{character}' is a vowel!")
else:
    print(f"The character '{character}' is a consonant!")
