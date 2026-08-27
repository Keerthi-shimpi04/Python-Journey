 #IF -Else statements..
'''
if condition:
    statement
'''
'''
age=int(input("Enter your age:"))

if(age>=18):
    print("You are eligible for a vote")
else:
   print("You are not eligible for a vote")
   '''


#elif statements....
day=int(input("Enter the the number from 1 to 7:"))

if(day==1):
    print("MONDAY")
elif(day==2):
    print("TUESDAY")
elif(day==3):
    print("WEDNESDAY")
elif(day==4):
    print("THURSDAY")
elif(day==5):
    print("FRIDAY")
elif(day==6):
    print("SATURDAY")
else:
    print("SUNDAY")


#Nested if Conditions..
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Not eligible")