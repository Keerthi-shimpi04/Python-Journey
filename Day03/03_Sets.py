#Sets: Unordered,no duplicate values,no indexing,mutable

numbers={1,1,2,3,4,2,3,4,5,6}
print(numbers) #{1,2,3,4,5,6} is a output 


#Why sets are useful??

students = ["Rahul", "Priya", "Rahul", "Ananya", "Priya"]
unique_students=set(students)
print(unique_students)


# Set Operations::

# 1. Union:

a={1,2,3,4,5,2}
b={7,8,9,10}
print(a|b) #a union b


# 2.Intersection:
a={1,2,3,4,5,2}
b={7,8,9,4,5,10}
print(a&b) # a intersection b


# 3.Difference:
a={1,2,3,4,5,2}
b={7,8,9,4,5,10}
print(a-b)
print(b-a)

# 4.Symmetric Difference:Elements that are in either set, but not both
a={1,2,3,4,5,2}
b={7,8,9,4,5,10}
print(a^b)
