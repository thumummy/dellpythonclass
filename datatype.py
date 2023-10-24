# data type

number = 100  # int
second = 56.78  # float
text = "hellow there"  # string
ispythoninteresting = "true"  # b00l

# data type storering multiple values in a variable
cars = ["toyota","nissan","vw"]  # list
fruits = ("banana","apples","oranges")  # tuple
countries = {"kenya","uganda","algeria","tunisia"}  # set
detail = {
    "firstname": "fatuma",
    "age": 21,
    "course": "web development",
    "nationality": "kenyan"
} #Dictionary

print(detail["firstname"])
print(detail["age"])
print(second)
print(text)
print(cars)
print(countries)

# Determine a data type
print(type(text))
print(type(countries))
print(type(detail))
print(type(fruits))

# typecasting - is converting one data type to another
print(float(number))
print(int(second))
print(str(ispythoninteresting))

