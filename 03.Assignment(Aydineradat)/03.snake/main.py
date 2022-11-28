import random
n = int(input("plz enter the length of your array:"))


for i in range(n):
    if i % 2 == 0:
        print("*", end="")
    if i % 2 != 0:
        print("#", end="")



