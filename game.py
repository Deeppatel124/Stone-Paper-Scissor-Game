import random

def game():
    print(" Welcome to Stone   Paper   Scissors  !")
    options = ["stone", "paper", "scissors"]
    user = input("Enter your choice (stone/paper/scissors): ").lower()

    if user not in options:
        print(" Invalid choice! Please choose stone, paper, or scissors.")
        return

    computer = random.choice(options)
    print(f" Computer chose: {computer}")

    if user == computer:
        print(" It's a tie!")
    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        print(" You win! ")
    else:
        print(" You lose!")


game()