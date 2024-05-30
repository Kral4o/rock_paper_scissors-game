import random

while True:
    computer_choice = ["rock", "paper", "scissors"]
    computer_input = random.choice(computer_choice)

    print("rock,paper,scissors... SHOOT:", end=" ")
    player_input = input()

    while player_input not in computer_choice:
        print("Incorrect input.")
        print("Try again:", end=" ")
        player_input = input()

    if player_input == computer_input:
        print(f"{player_input} : {computer_input}")
        print("DRAW")
    elif player_input == "rock" and computer_input == "scissors":
        print(f"{player_input} : {computer_input}")
        print("Player wins")
    elif player_input == "rock" and computer_input == "paper":
        print(f"{player_input} : {computer_input}")
        print("Computer wins")
    elif player_input == "paper" and computer_input == "scissors":
        print(f"{player_input} : {computer_input}")
        print("Computer wins")
    elif player_input == "paper" and computer_input == "rock":
        print(f"{player_input} : {computer_input}")
        print("Player wins")
    elif player_input == "scissors" and computer_input == "rock":
        print(f"{player_input} : {computer_input}")
        print("Computer wins")
    elif player_input == "scissors" and computer_input == "paper":
        print(f"{player_input} : {computer_input}")
        print("Player wins")

    print("Play Again?")
    print("(y/n):", end=" ")

    command = input()

    if command == "y":
        pass
    elif command == "n":
        print("GAME OVER")
        break
    else:
        print("Invalid input")
        break
