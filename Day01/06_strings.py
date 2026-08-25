#Strings are the sequence of characters. Strings are immutable in python. Strings are defined in single quotes or double quotes.Strings are iterable in python.We can access the characters of string using indexing and slicing. Strings are also called as str class in python.

#String concatenation: combining two or more strings together using + operator
first_name="Keerthi"
Last_name="Shimpi"
full_name=first_name+" "+Last_name
print(full_name)

a="Dayanada Sagar"
b="College of Engineering"
c=a+" "+b
print(c)


#STRING INDEXING:
name="Keerthi"
print(name[1])
print(name[2])
print(name[3])
'''
 P  y  t  h  o  n
 0  1  2  3  4  5 

 AND 
NEGATIVE INDEXING
  P  y  t  h  o  n 
-6 -5 -4 -3 -2 -1
'''
print(name[-2])

# STRING SLICING-To access a range of characters in a string...syntax is string_name[start:end:step] where end is excluded and step is optional....

Word="Supercalifragilisticexpialidocious"
print(Word[0:5]) #Super here the 5th index is not included....
print(Word[-2:-6]) #This will print an empty string because the start index is greater than the end index.Usually the slicing is done from left to right but we can slice but we will provide the step=-1 to slice from right to left


print(Word[-2:-6:-1]) #This will print the characters from index -6 to -2 in reverse order because we have provided the step=-1.the output is uoic.


print(Word[-6:-2:1]) #This will print ocio. step =1 means we are moving from left to right but the start index is -6 and end index is -2 so it will print the characters from index -6 to -2 in left to right order.

print(Word[3:]) #ercalifragilisticexpialidocious
print(Word[:7]) #Superca


#If we want to reverse the string we can use step=-1 in slicing.

print(Word[::-1]) #suoicodilaipxecitsiligarfilacrepuS

#**** STRINGS ARE IMMUTABLE IN PYTHON***- strings can never be changed once they are created.If we want to change we have to create new string.

#name="keerthi"
#name[1]='i'Here the above line will give an error because strings are immuatable.


'''
STRING METHODS: Python provides many builtin methods to perform operations on strings. some of the commonly used are:
1.Len() method:returns the length of the string.
 Example: 
   print(len("Prathaam"))
2.upper() method:returns the string in uppercase.
3.lower() method: returns the string in lowercase.
4.strip() method:returns the string after removing the leading and trailing whitespaces.
5.replace() method:returns the string by replacing the old substring with the new substring.
6.split() method: returns a list of substrings by splitting the string at the specified separator
7.join() method:returns a string by joing the elements of the iterable with the specified separator
8.find() method:returns the index of the first occurances of the specified substring in the string.If it is not found it returns -1.
9.count() method:returns the number of occurances of the specified substring in the string.
10..startswith() method:return true or false if the string starts with the specified substring.

'''

print(len("Prathaam")) #8
print("Prathaam".upper()) #PRATHAAM
print("PRATHAM".lower()) #pratham
print("  pratham  ".strip()) #pratham
print("Prathaam".find("tha")) #3
print("Prathaam".count("a")) #2
print("Prathaam".startswith("Pr")) #True
print("pratham".replace("pr","Krr")) #Krratham
print("pratham is a good boy".split())
#print({"pratham","lives","in","smg"}.join()) #this is showing error 
#print(" ".join({"pratham", "lives", "in", "smg"})) #smg lives in pratham...Set is unordered
print(" ".join(["pratham", "lives", "in", "smg"])) #pratham lives in smg its inside the list (order is preserved)..

# f-strings:This string contains expressions that should be evaluated.
name = "Keerthi"
age = 21

print(f"My name is {name} and I am {age} years old.")

a = 10
b = 20

print(f"The sum is {a + b}")


# Expression produces value and statement performs an action...