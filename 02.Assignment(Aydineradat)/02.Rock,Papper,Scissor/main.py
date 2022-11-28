
import random

user_score = 0
cp_score = 0
while user_score < 5 and cp_score < 5:
    x = random.randint( 1 , 3 )

    if x == 1:
        cp_choice = "rock"
    elif x == 2:
        cp_choice = "paper"
    elif x == 3:
        cp_choice = "scissor"

    user_choice = int(input("Plz choose number (1.rock 2.paper 3.scissor) : "))


    if user_choice == 1:
        user_choice = "rock"
    elif user_choice == 2:
        user_choice = "paper"
    elif user_choice == 3:
        user_choice = "scissor"
    print("computer choice : " , cp_choice)
    print("Your choice: " , user_choice)

    if (cp_choice == "paper" and user_choice == "rock") or (cp_choice == "rock" and user_choice == "scissor") or ( cp_choice == "scissor" and user_choice == "papper"):
        cp_score += 1
        print("cp wins ","Your score:", user_score , "computer score:" , cp_score)
    elif ( user_choice == "paper" and cp_choice == "rock") or ( user_choice == "rock" and cp_choice == "scissor") or ( user_choice == "scissor" and cp_choice == "paper"):
        user_score += 1
        print("you win " , "Your score:", user_score , "computer score:" , cp_score)
    elif ( user_choice == "paper" and cp_choice == "paper") or ( user_choice == "rock" and cp_choice == "rock") or ( user_choice == "scissor" and cp_choice == "scissor"):
        print("you choose the same item ", "Your score:", user_score , "computer score:" , cp_score)

