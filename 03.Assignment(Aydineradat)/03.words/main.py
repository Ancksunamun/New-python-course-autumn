import re
print("Hello our program counts your words")
str = input("PLz enter your words: ")

result = re.sub(' +', ' ', str)

new = result.strip().split(" ")

print("Number of your words: " , len(new))

