

name = input("Plz enter your name: ")
family = input( "Plz enter your family name: ")
a = int(input("Please inter your first grade: "))
b = int(input("Please inter your second grade: "))
c = int(input("Plz enter your third grade: "))
av = (a + b + c) / 3

if av >= 17:
    print (name , family ,"your average is", av , "you are great")

if 17 > av >= 12:
    print(name , family ,"your average is", av , "you should work harder man")

if 12 > av :
    print(name , family ,"your average is", av , "you should ponder about your future immediately")