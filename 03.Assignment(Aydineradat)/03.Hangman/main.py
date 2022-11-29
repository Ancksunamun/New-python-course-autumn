import random

word_bank = ["hossein", "jabbar", "jaber", "nikka", "women", "life", "freedom", "hadis"]

x = random.randint(1, len(word_bank)-1)
counter = 6
word = word_bank[x]

right_char = []
wrong_char = []
win_array = []

for i in range(len(word)):
    if word[i] not in win_array:
        win_array.append(word[i])



while counter != 0:
    for i in range(len(word)):
        if word[i] in right_char:
            print(word[i], end=" ")
        else:
            print("_ ", end="")

    if win_array == right_char:
        print("Congratulations , You win")
        break
    user_char = input("Plz insert your guess: ")
    user_char = user_char.lower()
    if len(user_char) == 1:

        if user_char in word:
            right_char.append(user_char)
            print("Yes \nyou have", counter, "chances , wrong chars:", wrong_char)
        else:
            wrong_char.append(user_char)
            counter -= 1
            print("No \nyou have", counter, "chances wrong chars:", wrong_char)

    else:
        print("Insert only ONE word")



if counter == 0:
    print("You lost , loser")