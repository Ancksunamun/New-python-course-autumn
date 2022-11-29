import math

operator = input("Plz enter your operator among these: + , - , * , / , sqrt(square root) , sin , cos , tan , cot , fac(factorial):")
if operator == "+" or operator == "-" or operator == "*" or operator == "/":
    a = float(input("Please enter your first number:"))
    b = float(input("Please enter your second number:"))

    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        if b != 0:
            result = a / b
        else:
            result = "Division by zero error"

elif operator == "sqrt" or operator == "sin" or operator == "cos" or operator == "tan" or operator == "cot" or operator ==  "fac":
    a = float(input("Plz enter your number:"))
    if operator == "sqrt":
        result = math.sqrt(a)
    if operator == "sin":
        result = math.sin(math.radians(a))
    if operator == "cos":
        result = math.cos(math.radians(a))
    if operator == "tan":
        result = math.tan(math.radians(a))
    if operator == "cot":
        result = math.tan(math.radians(a)) ** -1
    if operator == "fac":
        result = math.factorial(int(a))


else:
    result = ("The operation you have chosen is unavailable in our calculator")



print("result = ",result)


