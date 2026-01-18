""" Rock Paper Scissors Game
Pedro Quintela
1/16/2026
Creates an interface that the user can interact with in order to play the game, also the main function for the game.
"""

import random

# Randomly picks the opponents choice from the choices list.
def gen_opp():

    # Possible choices for the opponent to randomly get assigned.
    choices = ["Rock", "Paper", "Scissors"]

    # Returns the randomly picked move.
    return random.choice(choices)


# Compares the user's choice to the opponent's random move.
def compare(user: str):

    # Assigns the opponent's randomly picked move then assigns a different vairbale a completely lowercased version to be used in the if statements
    generated_opp = gen_opp()
    opponent = generated_opp.lower()
    
    # Prints the opponent's choice using the first version
    print("\nYour opponent has picked... " + generated_opp)

    # Checks every possible outcome to determine the result of the two choices.
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


# Main choices for the game
def game_choices():

    print("---------------------- Choices ----------------------")
    print("1) Rock \n2) Paper \n3) Scissors\n")

    # Makes sure that any non-integer choices get caught and notifies the user and allows them to try again.
    try:
        # Asks the user for an input relating to the options above.
        user_input = int(input("Please Choose an Option Above - "))

        # Calls the compare funciton depending on the user's choice.
        if user_input == 1:
            compare("rock")
    
        elif user_input == 2:
            compare("paper")

        elif user_input == 3:
            compare("scissors")
    
        else:
            # Catches an incorrect number choice and has the user retry by calling the function again.
            print("\nInvalid Choice, Please Try Again.\n")
            game_choices()
    
    except ValueError:
        print("Please only input a number!\n")
        game_choices()
    
    # Returns back to the first prompt after the round is over.
    interface_main()


# First prompt the user will get
def interface_main():

    print("---------------------- Play Game ----------------------")
    print("1) Play \n2) End Program \n")

    # Makes sure that any non-integer choices get caught and notifies the user and allows them to try again.
    try:
        main_input = int(input("Please Choose an Option Above - "))

        # Continues depending on the user's choice.    
        if main_input == 1:
            game_choices()

        elif main_input == 2:

            return

        else:
            # Catches an incorrect number choice and has the user retry by calling the function again.
            print("Invalid Choice, Please Try Again.\n")
            interface_main()
    
    except ValueError:
        print("Please only input a number!")
        interface_main()

    return
   