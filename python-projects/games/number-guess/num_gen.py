""" Number Generator
Pedro Quintela
1/16/2026
Generates a random number between the minimum and maximum inputted by the user and stores it.
"""

import random

def generate_number(min: int, max: int) -> int:

    # Base cases
    if min > max:

        print("The minimum needs to be less than the maximum")
        return

    elif min == max:

        print("Hey, no cheating! There is only one possible number\n")
        print("Please make the minimun and maximum different numbers")
        return

    elif min < 0:

        print("Sorry! Please remember not to input negative numbers.")
        return

    # Generates the number randomly using the parameters
    random_result = random.randint(min, max)

    return random_result


def num_main() -> int:

    # Asks the user to input the minimum & maximum to continue the function
    print("\n---------------------------------------------------------------------\n")
    print("\nPlease input the following to start - \n")
    user_min = int(input("Minimum: "))
    user_max = int(input("Maximum: "))

    # Stores the randomly generated number
    stored_num = generate_number(user_min, user_max)

    # Returns the generated number to be used in the game
    return stored_num