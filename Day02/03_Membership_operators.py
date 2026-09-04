#Identity Operator:

#is and is not are the two identity operators...

str1="Keerthi"
str2="Keerthi"

print(str1 is str2) #True memory loacation uses same location in case if the data is same..Identity operator compares the memory location whereas "==" compares the value

str1="Keerthi"
str2="Keerthis"
print(str1 is not str2) #True


#Membership operators:

#in and not in are two membership operators

str="Ganapati"
print('G'in str)  #True
print('G'not in str) #False
print('e'in str) #False

list=[10,20,30,-1]

print(10 in list)
print(0 in list)
print(0 not in list)




