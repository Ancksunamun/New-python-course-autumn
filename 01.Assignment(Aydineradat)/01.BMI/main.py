
height = int(input("Plz enter your Height: "))
weight = int(input("Plz enter your Weight: "))

bmi = weight / (height/100) ** 2

if bmi < 18.5:
    print("Your BMI index is:" , bmi , "You are underweight")

elif 25 > bmi >= 18.5:
    print("Your BMI index is:" , bmi , "You are in good shape")

elif 30 > bmi >= 25:
    print("Your BMI index is:" , bmi , "You are relatively overweight")

elif  35 > bmi >= 30:
    print("Your BMI index is:" , bmi ,"You are Obese")

elif  bmi >= 35:
    print("Your BMI index is:" , bmi , "You are extremely obese you should go and see a doctor")

