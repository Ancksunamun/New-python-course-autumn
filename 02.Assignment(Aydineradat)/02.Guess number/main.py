
print("Hi, Welcome to our guessing number game")
import random
cp_number = random.randint( 10 , 40 )
user_number = int(input("Plz enter your number between 10 and 40 (10 and 40 included)"))

counter = 0
while True:

    if cp_number == user_number:
        counter += 1
        print("you are right our number is:" , cp_number)
        print("you have tried:" , counter , "times")
        break
    elif cp_number > user_number:
        counter += 1
        print("go Higher")
    elif cp_number < user_number:
        counter += 1
        print("go Lower")
    user_number = int(input())


