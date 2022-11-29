print("If you finished print 0")
nums = []

while True:
    n = int(input("Plz enter your numbers:"))
    if n == 0:
        break
    else:
        nums.append(n)
print(nums)
nums = list(dict.fromkeys(nums))
print(nums)