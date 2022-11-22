
counter = 0
b = 0
while True:
    a = input("Plz enter your grades and if you finished type exit:")
    if a != "exit":
        b += int(a)
        counter += 1
    elif a == "exit":
        break

print("your average is:" , b / counter )




