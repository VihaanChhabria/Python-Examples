import random

Human = 0
Computer = 0

shoot = ["rock", "paper", "scissors"]
while True:
    choice = input("Rock, Paper, Scissor, Shoot! ")
    choice = choice.lower()
    computer_choice = random.choice(shoot)
    print(computer_choice)

    if (choice == "rock") and (computer_choice == "paper"):
        Human = Human + 1
        print("Human Points: " + Human)
        print("Computer Points: " + Computer)
        print("Human Wins!")

    if (computer_choice == "rock") and (choice == "paper"):
        Computer = Computer + 1
        print("Human Points: " + Human)
        print("Computer Points: " + Computer)
        print("Computer Wins!")

    if (choice == "rock") and (computer_choice == "scissor"):
        Human = Human + 1
        print("Human Points: " + Human)
        print("Computer Points: " + Computer)
        print("Human Wins!")

    if (computer_choice == "rock") and (choice == "scissor"):
        Computer = Computer + 1
        print("Human Points: " + Human)
        print("Computer Points: " + Computer)
        print("Computer Wins!")

    if (choice == "paper") and (computer_choice == "scissor"):
        Human = Human + 1
        print("Human Points: " + Human)
        print("Computer Points: " + Computer)
        print("Human Wins!")

    if (computer_choice == "paper") and (choice == "scissor"):
        Computer = Computer + 1
        print("Human Points: " + Human)
        print("Computer Points: " + Computer)
        print("Computer Wins!")

    if (computer_choice == choice):
        print("Human Points: " + Human)
        print("Computer Points: " + Computer)
        print("Tie!")