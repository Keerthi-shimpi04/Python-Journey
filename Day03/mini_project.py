import random


print("======== Rock,Paper,Scissor Game =========")

while(True):

    print("Enter 0 for Rock")
    print("Enter 1 for Paper")
    print("Enter 2 for Scissor")

    user_choice=int(input("Enter your choice:"))

    computer_choice=random.randint(0,2)
    print("computer_choice:",computer_choice)


    if(user_choice<0 or user_choice>2):
        print("Invalid choice...")

    elif(user_choice==computer_choice):
        print("Ohh no!! We both are equal")

    elif(computer_choice>user_choice):
        print("ohh noo you lose 😭")

    elif(user_choice>computer_choice):
        print("Congratulations... You won 🥳🥳🥳")

    elif(user_choice==0 and computer_choice==2):
        print("You win!!🥳🥳🥳😁")

    elif(user_choice==2 and computer_choice==0):
        print("You lose😞😞😞")
