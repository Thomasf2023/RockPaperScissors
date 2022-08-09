#Rock_Paper_Sissors
#The purpose of this project is to create a rock paper scissors game.
#Author: Thomas Fiske
#Date: 8/9/2022

import random

def play():
    user_move = input("Enter a choice (rock, paper, scissors): ")
    moves_list = ["rock", "paper", "scissors"]
    computer_move = random.choice(moves_list)
    print(f"\nYou chose {user_move}, computer chose {computer_move}.\n")

    if user_move == computer_move:
        print(f"Both players selected {user_move}. It's a tie!")
    elif user_move == "rock":
        if computer_move == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_move == "paper":
        if computer_move == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_move == "scissors":
        if computer_move == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

play()
