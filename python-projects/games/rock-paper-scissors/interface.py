""" Rock Paper Scissors Interface
Pedro Quintela
1/16/2026
Creates an interface that the user can interact with in order to play the game, also the main function for the game.
"""

import random

def gen_opp():

    choices = ["Rock", "Paper", "Scissors"]

    return random.choice(choices)


def compare(user: str):

    generated_opp = gen_opp()
    opponent = generated_opp.lower()
    
    print("\nYour opponent has picked... " + generated_opp)

    if user == "rock":

        if opponent == "rock":
            print("Draw!")

        elif opponent == "paper":
            print("You Lose..")

        elif opponent == "scissors":
            print("You Win!!")

    elif user == "paper":

        if opponent == "rock":
            print("You Win!!")

        elif opponent == "paper":
            print("Draw!")

        elif opponent == "scissors":
            print("You Lose..")

    elif user == "scissors":

        if opponent == "rock":
            print("You Lose..")

        elif opponent == "paper":
            print("You Win!!")

        elif opponent == "scissors":
            print("Draw!")

    else:
        print("Seems like you didn't enter one of the correct options.\n")
        
    return


def game_choices():

    print("---------------------- Choices ----------------------")
    print("1) Rock \n2) Paper \n3) Scissors\n")

    try:
        user_input = int(input("Please Choose an Option Above - "))

        if user_input == 1:
            compare("rock")
    
        elif user_input == 2:
            compare("paper")

        elif user_input == 3:
            compare("scissors")
    
        else:
            print("\nInvalid Choice, Please Try Again.\n")
    
    except ValueError:
        print("Please only input a number!\n")
        game_choices()

    
    
    interface_main()


def interface_main():

    print("---------------------- Play Game ----------------------")
    print("1) Play \n2) End Program \n")

    try:
        main_input = int(input("Please Choose an Option Above - "))

        if main_input == 1:
            game_choices()

        elif main_input == 2:

            return

        else:
            print("Invalid Choice, Please Try Again.\n")
            interface_main()
    
    except ValueError:
        print("Please only input a number!")
        interface_main()

    

    return
   