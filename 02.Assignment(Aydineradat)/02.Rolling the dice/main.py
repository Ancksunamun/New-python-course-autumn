import random

dice =  random.randint( 1 , 6 )
print("your number on dice is:" , dice)
while dice == 6:

    dice = random.randint( 1 , 6 )
    print("you are lucky your prize is:", dice)
