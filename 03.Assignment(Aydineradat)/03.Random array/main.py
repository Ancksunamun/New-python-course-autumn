
import random

n = int(input("Plz enter how many elments do you need: "))
list = []
counter = 0

while counter < n:
    d = random.randint(1,99)
    list.append(d)
    counter += 1

print(list)