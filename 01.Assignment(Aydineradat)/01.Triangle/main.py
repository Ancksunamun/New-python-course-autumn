
a = float(input("plz enter first angle:"))
b = float(input("plz enter second angle"))
c = float(input("plz enter second angle"))

if a + b > c and b + c > a and a + c > b:
    print("this can be a triangle")
else:
    print("you cant draw triangle with the angles")