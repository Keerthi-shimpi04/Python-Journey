#Challenge_01

#STUDENT's GRADE CLACULATOR:
'''
Marks=int(input("Enter your Marks:"))

print(Marks)

if(Marks<0 or Marks>100):
    print("Invalid Marks.Enter the valid Marks...")

elif(Marks>=90):
    print("'A' Grade")
elif(Marks>=75):
    print("'B' Grade")
elif(Marks>=60):
    print("'C' Grade")
elif(Marks>=40): 
    print("'D' Grade")
else:
    print("FAIL")
'''
#Challenge_02

#Login System
'''
Username=input("Enter your username:")
Password=input("Enter your password:")

if(Username=="Admin" and Password=="1234"):
    print("Successfully loggined....")
else:
    print("Invalid username Try next time...")
'''


#Challenge_03
'''
for i in range(1,20):
    print(i)

for i in range(1,20,2):
    print(i)


for i in range(20,0,-2):
    print(i)
'''

#Challenge_04
'''
word=input("Enter one word:")
print(word)
count=0

for character in word:
    if(character=='a'or character=='e' or character=='i' or character=='o' or character=='u'):
     count=count+1
     
print("Vowels present are:",count)      
'''

# Challenge_05

#NUMBER GUESSING GAME
'''

Secret_Key = 765
user=int(input("Enter the number to guess the secret key:"))

while(True):
    if(user!=765):
     print("OHH NOO!!....TRY AGAIN")


    else:
     print("CONGRATULATIONS!!!!!")
     '''

#CORRECT VERSION

Secret_Key = 765

while True:

    user = int(input("Enter the number to guess the secret key: "))

    if user != Secret_Key:
        print("OHH NOO!!....TRY AGAIN")

    else:
        print("CONGRATULATIONS!!!!!")
        break