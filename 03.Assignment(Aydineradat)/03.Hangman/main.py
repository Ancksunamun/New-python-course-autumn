import random

word_bank = ["hossein" , "jabbar" , "jaber" , "nikka" , "women" , "life" , "freedom" , "hadis"]

x = random.randint(1, len(word_bank)-1)
counter = 6
word = word_bank[x]

right_char = []
wrong_char = []

print(word)
# for i in range(len(word)):
#     print("_ ", end="")
while counter != 0:
    for i in range(len(word)):
        if word[i] in right_char:
            print(word[i], end="")
        else:
            print("_ ", end="")
    user_char = input("Plz insert your guess: ")
    user_char = user_char.lower()
    if len(user_char) == 1:

        if user_char in word:
            right_char.append(user_char)
            print("Yes")
        else:
            wrong_char.append(user_char)
            print("No")
            counter -= 1
            print(counter)
    else:
        print("Insert only ONE word")