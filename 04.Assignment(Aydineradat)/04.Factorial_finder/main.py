
import math

n = int(input("Plz enter your number:"))
factorial = 0
counter = 1
while factorial < n:
    factorial = math.factorial(counter)
    counter += 1


if factorial == n:
    print("This is a factorial number")
else:
    print("this is not a factorial number")
