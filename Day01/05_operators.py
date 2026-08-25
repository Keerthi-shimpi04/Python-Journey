# Artimetic Operators:
"""+    Addition
-    Subtraction
*    Multiplication
/    Division
//   Floor division
%    Modulus
**   Exponentiation"""


a=25
b=5

print(a+b) #30
print(a-b) #20
print(a*b) #125
print(a/b) #5.0
print(a//b) #5 floor division is ex 10/3=3.333 but floor division is 3
print(a%b) #0
print(a**b) #97,65,625 (25^5)


#Comparison Operators:
"""== Equal to
!= Not equal to
< Less than
> Greater than
<= Less than or equal to
>= Greater than or equal to"""


# "=" is an assignment operator which is used to assign the value to the variable
# "==" is a comparison operator which is used to compare the values of two variables and returns the boolean value


age= 34
print(age==34) #True It returns the boolean Value
print(age!=34) #False
print(age<34) #False
print(age>34) #False
print(age<=34) #True
print(age>=34) #True


#Logical Operators:
"""and Returns TRUE if both statements are true
or Returns TRUE if one of the statements is true
not Reverse the result, returns False if the statement is True"""

has_ticket=True
is_vip=False
print(has_ticket and is_vip) #False
print(has_ticket or is_vip) #True
print(not has_ticket) #False