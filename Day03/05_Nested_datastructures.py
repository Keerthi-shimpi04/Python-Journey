#List of dictionaries:

students = [
    {"name": "A", "marks": 90},
    {"name": "B", "marks": 85},
    {"name": "C", "marks": 95}
]
print(students)
print(students[0:2])
print(students[0]["name"])
print(students[0]["marks"])



# Dictionary containg lists:

student = {
    "name": "Keerthi",
    "skills": ["Python", "SQL", "DSA"]
}

#print(student["skills"][1,3]) if we want more than one indices just slice it...
print(student["skills"][0:2])

for skill in student["skills"]:
    print(skill)


'''
SUMAMARY:
Ordered collection that changes	- List
Fixed ordered collection - Tuple
Unique values -	Set
Key → value relationship -	Dictionary




Shopping cart → List
GPS coordinates → Tuple
Unique email IDs → Set
Student information → Dictionary
'''