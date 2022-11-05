#Rock, Paper, Scissers
import random

Human = 0
Computer = 0
a = ["rock", "paper", "scissors"]
b = (random.choice(a))

while True:
    c = input("Rock, Paper, Scissors! ")
    print(b)

    if (b == "rock") and (c == "paper"):
        Human = Human + 1
        print("Human =",Human)
        print("Computer =",Computer)
        print("Human wins!")

    if (b == "paper") and (c == "rock"):
        Computer = Computer + 1
        print("Human =",Human)
        print("Computer =",Computer)
        print("Computer wins!")

    if (b == "paper") and (c == "scissors"):
        Human = Human + 1
        print("Human =",Human)
        print("Computer =",Computer)
        print("Human wins!")

    if (b == "scissors") and (c == "paper"):
        Computer = Computer + 1
        print("Couputer wins!")
        print("Human =",Human)
        print("Computer =",Computer)

    if (b == "rock") and (c == "scissors"):
        Computer = Computer + 1
        print("Human =",Human)
        print("Computer =",Computer)
        print("Couputer wins!")

    if (b == "scissors") and (c == "rock"):
        Human = Human + 1
        print("Human =",Human)
        print("Computer =",Computer)
        print("Human wins!")

    if (b == "rock") and (c == "rock"):
        print("Human =",Human)
        print("Computer =",Computer)
        print("A tie!")

    if (b == "paper") and (c == "paper"):
        print("Human =",Human)
        print("Computer =",Computer)
        print("A tie!")

    if (b == "scissors") and (c == "scissors"):
        print("Human =",Human)
        print("Computer =",Computer)
        print("A tie!")