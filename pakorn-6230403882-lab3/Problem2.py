i = 2
for i in range(2,-1,-1):
    word = str(input("Enter a word:"))
    if word == "kku":
        print("Congrats that you can guess the secret_word correctly")
        break
    else:
        print("Incorrect! you have", i,"guesses left.")
        print("Thank for trying, but the secret word is actullay kku")

