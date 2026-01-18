""" Number Guessing Game Interface
Pedro Quintela
1/16/2026
Creates an interface that the user can interact with in order to play the game. Also is the main function for the game.
"""

# Allows num_main from num_gen to be called in this code.
from num_gen import num_main

# Judges the user's guess to see if it was too low, too high, or correct based on the guess inputted and the generated number.
def judge_guess(guess: int, generated_num: int):

    # Base case, checking that the user's guess is not a negative number.
    if guess < 0:

        print("Whoops! Looks like you put an invalid number")
        print("Please remember, the number inputted cannot be a negative number")

        # Brings the user back to the choices prompt.
        choices_prompt(generated_num)
        return

    # Checks if the user has won.
    if guess == generated_num:

        # Brings the user to the winner prompt.
        win()
        return

    # Checks if the user's guess was too high.
    elif guess > generated_num:

        print("\n---------------------------------------------------------------------\n")
        print("Your guess is too high.. Try again!")

        # Brings the user back to the choices prompt.
        choices_prompt(generated_num)
        return

    # Checks if the user's guess was too low.
    elif guess < generated_num:

        print("\n---------------------------------------------------------------------\n")
        print("Your guess is too low.. Try again!")

        # Brings the user back to the choices prompt.
        choices_prompt(generated_num)
        return


# Provides the user with choices on how to proceed with the game while carrying the generated number in the parameter.
def choices_prompt(number):

    print("\n-------------- Choices --------------\n")
    print("1) Guess \n2) Generate a New Number \n3) End Program\n")

    # Makes sure that any non-integer choices get caught and notifies the user and allows them to try again.
    try:

        # Asks the user for an input relating to the options above.
        choice_input = int(input("Please Choose an Option Above - "))

        # Checks input to provide the correct path within the game.
        if choice_input == 1:

            # Asks the user for a guess input.
            guess_input = int(input("\nPlease enter your guess - "))
            # Calls the judge_guess function with the users input as the guess parameter while carrying the generated number as the other.
            judge_guess(guess_input, number)
            return

        elif choice_input == 2:

            # Generates a new number by calling the number generator function and assigning it to a variable.
            new_number = num_main()
            # Uses the variable as the parameter when going to the choices prompt to be carried along as the new generated number to be guessed.
            choices_prompt(new_number)
            return

        elif choice_input == 3:

            # Ends program by not giving the user any further options
            return

        else:

            print("Oops! Seems like you did not enter a valid input")
            print("Please enter either 1 or 2")

            # Reroutes the user back to the start of the choices prompt with the current generated number.
            choices_prompt(number)
            return

    except ValueError:
        print("Please only input a number!\n")
        choices_prompt(number)


# The winner prompt that the user gets after correctrly guessing the current generated number.
def win():

    print("\n<-------------------------------- Great Job! You have won the Number Guessing Game! -------------------------------->\n")
    print("1) Would you like to try again? \n2) End Program\n")

    # Makes sure that any non-integer choices get caught and notifies the user and allows them to try again.
    try:

        # Asks the user for an input relating to the options above.
        win_input = int(input("Please Choose an Option Above - "))

        # Checks input to provide the correct path within the game.
        if win_input == 1:

            # Generates a new number by calling the number generator function and assigning it to a variable.
            new_number = num_main()
            # Uses the variable as the parameter when going to the choices prompt to be carried along as the new generated number to be guessed.
            choices_prompt(new_number)
            return

        elif win_input == 2:

            # Ends program by not giving the user any further options
            return

        else:

            print("Oops! Seems like you did not enter a valid input")
            print("Please enter either 1 or 2")

            # Reroutes the user back to the start of the winner prompt.
            win_main()
            return

    except ValueError:
        print("Please only input a number!\n")
        win()


def interface_main():

    print("------------- Welcome to the Number Guessing Game! -------------\n")
    print("Start game - 1 \nEnd Program - 2\n")

    # Makes sure that any non-integer choices get caught and notifies the user and allows them to try again.
    try:

        # Asks the user for an input relating to the options above.
        start_input = int(input("Please Choose an Option Above - "))

        # Checks input to provide the correct path within the game.
        if start_input == 1:

            # Generates a number by calling the number generator function and assigning it to a variable
            inital_number = num_main()
            # Uses the variable as the parameter when going to the choices prompt to be carried along as the  generated number to be guessed.
            choices_prompt(inital_number)
            return

        elif start_input == 2:

            # Ends program by not giving the user any further options
            return

        else:

            print("Oops! Seems like you did not enter a valid input")
            print("Please enter either 1 or 2")

            # Reroutes the user back to the start of the starting prompt.
            interface_main()
            return

    except ValueError:
        print("Please only input a number!\n")
        interface_main()