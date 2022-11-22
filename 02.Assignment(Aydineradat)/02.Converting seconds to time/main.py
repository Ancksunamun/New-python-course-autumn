from math import *
seconds = int(input("plz enter your seconds: "))

print("your time is=" , floor(seconds/3600) , ":" , floor((seconds%3600)/60) , ":" , ((seconds%3600)%60) )