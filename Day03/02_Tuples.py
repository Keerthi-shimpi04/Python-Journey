#Tuples:ordered,indexed,supports slicing,allows duplicate values but immutable

numbers = (1, 2, 2, 3)
#numbers[0]=4 not supported because it is immuatable
print(numbers.count(2))
print(numbers.index(3))


#Tuples Unpacking:

person = ("Keerthi", 22, "Data Science")

name, age, branch = person

print(name)
print(age)
print(branch)

school=("Ravi","Anusha","Raghavi")

Hm,Teacher,Student=school

print(Hm) 
print(Teacher) 
print(Student) 