#Challenge_01

name=input("Enter the name:")
age=int(input("Enter your age:"))
college=(input("Enter your college name:"))
Branch=(input("Enter your Branch:"))
city=(input("Enter your city:"))

print(f"My name is {name}.I am {age} years old.I am studing in {college} college. I am {Branch} student.I lives in {city}")



#Challenge_02

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

print(num1+num2)
print(num1-num2)
print(num1/num2)
print(num1**num2)
print(num1//num2)
print(num1%num2)



#Challenge_03

string=input("Enter the string:")
print(string)

print(string.lower())
print(string.upper())
print(len(string))
print(string[0])
print(string[-1])
print(string[::-1])
print(string.split()) #Because .split() splits a string based on a separator, and by default the separator is whitespace.
print(list(string))



#Challenge_04
 
age=int(input("Enter your age:"))

print(age)
if(age<0):
   print("Enter proper age...")
else:
 print("your's Birth year is:",2026-int(age))
 print("your age after 5 years is:",age+5)
 print("your age after 10 years is:",age+10)


 
