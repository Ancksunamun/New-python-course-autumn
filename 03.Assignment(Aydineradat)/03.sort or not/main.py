print("welcome to our sort checking program plz enter your numbers and (exit) if you finished")

nums_array = []
while True:
    user_nums = input("plz enter your number:")
    if user_nums == "exit":
        break
    nums_array.append(int(user_nums))

d = False

for i in range(len(nums_array)-1):
    if nums_array[i + 1] < nums_array[i]:
        print("not sort")
        d = True
        break
        d = True

if d == False:
    print("it is sort")


