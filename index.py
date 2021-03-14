import random

while True:
    user_command = input("Enter a choice: Rock, Paper, Scissors! ")

    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_command}, computer chose {computer_action}.\n")

    if user_command == computer_action:
        print(f"Both players selected {user_command}. It's a tie!")
    elif user_command == "Rock":
        if computer_action == "Scissors":
            print("Rock smashes Scissors! You win!")
        else:
            print("Paper covers Rock! You lose.")
    elif user_command == "Paper":
        if computer_action == "Rock":
            print("Paper covers Rock! You win!")
        else:
            print("Scissors cuts Paper! You lose.")
    elif user_command == "Scissors":
        if computer_action == "Paper":
            print("Scissors cuts Paper! You win!")
        else:
            print("Rock smashes Scissors! You lose.")
            
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
