#Data Structures:
#List: A list stores multiple values in an ordered collection.They are ordered and mutable..Python uses zero-based indexing...Accessing through the index...


fruits = ["apple", "banana", "mango", "orange"]

#List Slicing

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[:])
print(numbers[::2])
print(numbers[::-1]) # Reserves the list

# Lists are Mutable 
#fruits = ["apple", "banana", "mango", "orange"]

#fruits[0]="Custard apple"

print(fruits)


# List Operations:

# Contenation:
fruits=["Banana","Mango","Apple","Pappaya"]
vegetables=["Carrot","Potato","Beans","Beetroot"]

print(fruits+vegetables)

# Repetition

numbers=[1,2,3]
print(numbers*3)

# Membership
fruits=["Banana","Mango","Apple","Pappaya"]

print("Mango" in fruits)
print("Mango" not in fruits)


# List Methods:

# append():Adds one item at the end

jobs=["AI","Data scientist"]

jobs.append("Data Analyst")
print(jobs)

# insert():Adds the item at a particular position

numbers=[1,2,3,4]

numbers.insert(1,100)
print(numbers)

# extend():Adds multiple elements

numbers.extend([5, 6, 7])
print(numbers)

#numbers.append([6,7]) #[1, 100, 2, 3, 4, 5, 6, 7, [6, 7]]
#print(numbers)


# remove():
numbers.remove(4) 
print(numbers)# it removes the first occurance of 4 syntax:variable.remove(item)

# pop():Removes the last element

numbers.pop()
print(numbers)

numbers.pop(2)
print(numbers) #[1, 100, 3, 5, 6] it removes the value at index

#remove(value),pop(index)
  


# sort():
sets=[40,55,2,44,99]

sets.sort() # Ascending order by default
print(sets)
sets.sort(reverse=True) # Descending order
print(sets)

# reverse():it reverses the existing list

Tables=[2,4,6,8,10,12,14,16,18,20]
Tables.reverse()
print(Tables)


# Count(value): It counts the value occurances 
Tables=[2,4,6,5,5,8,10,10,12,14,16,18,20]

print(Tables.count(5))

# index(value): it returns the index of first occurance of the value
print(Tables.index(10))

# len():number of elements

print(len(Tables))   #Because len() is a built-in Python function, not a list method. its not numbers.len()


# Difference between sort() and sorted()

Numbers=[22,10,33,2,45]
print(sorted(Numbers))
print(Numbers) # sorted () it creates new list but sort() changes the original list



