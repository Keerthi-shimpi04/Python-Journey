# NUMBER GUESSING GAME:


print("WELCOME TO NUMBER GUESSING GAME!!")
print("You should guess a number between 1 to 100")

secret_number=88

attempts=0

while(True):
    user=int(input("Enter guess:"))

    if(user<=0 or user>=100):
        print("Ohh no u crossed the boundary...Guess the number from 1 to 100..")
        attempts+=1
        
       
    elif(user>secret_number):
     print("It's too high!!")
     attempts+=1
    
    elif(user<secret_number):
       print("It's too low!!")
       attempts+=1
       
    elif(user==secret_number):
       print("Congrats!! You guess it....")
       attempts+=1
       print(f"You guessed it in {attempts} attempts...")
       break


