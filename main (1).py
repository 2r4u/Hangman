import random, time, json

f = open("words.json", "r")
words = json.load(f).get("words")

def setup():
    global word, letters, hmp, y, rgsd, lt, gsd
    word = random.choice(words)
    letters = list(word)
    hmp = 0
    y = 0
    rgsd = [" "]
    lt = len(letters)
    gsd = ["_"] * lt

setup()
print("Welcome to Hangman!")

def prompt(q):
    p = input(q).lower()
    if p == "y" or p == "yes": return True
    elif p == "n" or p == "no": return False
    else:
        print("Say either yes or no")
        return prompt(q)

while True:
    if "_" in gsd:
        def display():
            print("Hangman at stage", hmp)
            print("Incorrect Letters:", *rgsd)
            l1, l2, l3, l4, l5 = ("  _____", "/", "|", "|", "---")
            if hmp >= 1:
                l2 += "    ⬤"
            if hmp == 2:
                l3 += "    |"
            if hmp == 3:
                l3 += "   /| "
            if hmp >= 4:
                l3 += "   /|\ "
            if hmp == 5:
                l4 += "   /"
            if hmp == 6:
                l4 += "   / \\"
                print(l1, "\n", l2, "\n", l3, "\n", l4, "\n", l5)
                print("YOU LOSE")
                print("Your word was: ", word)
                time.sleep(2)
                playa = prompt(
                    "Thanks for playing hangman. Would you like to play again? (y/n)"
                )
                if playa: setup()
                else:
                    time.sleep(2)
                    exit()
            print(l1, "\n", l2, "\n", l3, "\n", l4, "\n", l5)
            print("Your word is:")
            print(*" ".join(gsd), "\n\n")

        display()
        guess = input("Guess a letter: ")
        if not guess:
            print("Please provide a letter")
            continue
        guess = guess.strip().lower()
        if len(guess) > 1:
            print("One letter at a time please")
            continue
        if guess in rgsd:
            print("You already guessed that letter")
            continue
        if guess in letters:
            print(guess, "was correct")
            for i in range(len(letters)):
                if letters[i] == guess:
                    gsd[i] = guess
        else:
            print("nope")
            rgsd.append(guess)
            hmp += 1
    else:
        print("YOU WIN!")
        print("Your word was:", word)
        time.sleep(2)
        playa = prompt(
            "Thanks for playing hangman. Would you like to play again? (y/n)")
        if playa: setup()
        else:
            time.sleep(2)
            exit()