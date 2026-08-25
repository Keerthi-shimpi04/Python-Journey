"""
Data Types in python
1. Integer values:int
2. Floating point values:float
3. String values:str
4. Boolean values:bool
 
 None is a special data type in python which represents the absence of value or a null value"""

result=None

#type() is a built-in function which is used to check the data type of a variable

age=23
print(type(age)) #<class 'int'> becomes the object of int class

name="keerthi"
print(type(name))

height=5.2
print(type(height))

is_student=True
print(type(is_student))

print(type(result))

#Python is a dynamically typed language which means we dont need to declare the dat type of variable explicitly...

x=10
print(x)
x="Hello"
print(x)
x=3.14
print(x)


#TYPE CASTING: converting one data type to another data type...
age="23"
print(type(age)) #<class 'str'>

age=int(age)
print(type(age)) #<class 'int'>

x="Hello"
#x=int(x) #ValueError: invalid literal for int() with base 10:'hello' becoz is not a number to convert to int...

# SOME COMMON CONVERSIONS:
# int to float:
age=23
print(float(age)) #23.0

# float to int:
height=5.2
print(int(height)) #5

# int to str:
age=42
print(str(age)) #42

# str to float:
price="19.99"
print(float(price)) #19.99

# str to bool:
is_student="Yes"
print(bool(is_student)) #True becoz an non empty string is considered as True in python
print(type(bool(is_student))) 


is_employee=""
print(bool(is_employee)) #False becoz an empty string is considered as False in python


print(bool("False")) #True becoz the string "False" is not empty

is_car=False
print(bool(is_car))

