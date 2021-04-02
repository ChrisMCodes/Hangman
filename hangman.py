import random

def hangman(word):
    wrong = 0
    stages = ["",
             "_________       ",
             "|        |      ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))

words = ["abductions", "amplitudes", "background", "byproducts",
         "campground", "coequality", "downstream", "dormancies",
         "earthlings", "educations", "flamingoes", "flourished",
         "glamorized", "grievously", "harmonizes", "hysterical",
         "impersonal", "interlocks", "jackfruits", "judgmental",
         "labyrinths", "longitudes", "lunchmeats", "logarithms",
         "miscounted", "modulating", "nightclubs", "narcolepsy",
         "outlanders", "overacting", "pitchforks", "precaution",
         "redactions", "reductions", "relocating", "roundtable",
         "scrambling", "shoplifter", "tambourine", "throwbacks",
         "unimproved", "unscramble", "upholstery", "vanquished",
         "vibraphone", "whiteboard", "wingspread"]
         
         
         
         
         
         
hangman(random.choice(words))
