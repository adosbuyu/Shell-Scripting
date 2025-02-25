import random

def get_user_choice():
    user_choice = input("Enter rock, paper, or scissors: ").strip().lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
        user_choice = input("Enter rock, paper, or scissors: ").strip().lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    play_game()
