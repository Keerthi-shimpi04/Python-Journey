# Dictionary:stores key->value pairs
student = {
    "name": "Keerthi",
    "age": 22,
    "branch": "Data Science"
}

print(student["name"])
print(student["age"])
print(student["branch"])

#Add a new key
student["City"]="Bangalore" 
print(student)


#modify
student["age"]=23
print(student)

#delete

student.pop("age")
print(student)


'''
Dictinaries Methods:
keys()
values()
items()
get()
update()
pop()
popitem()
clear()
'''

print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)
