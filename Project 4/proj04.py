"""
    Project 4

    Algorithm
        Prompt to pick an option
            Match the option to a function
            If function requires any, prompt for an argument
            Evaluate the function with the passed argument
            Compare the result with the math module values
            Print the result, the math module value, and the difference
        Repeat
"""

import math

EPSILON = 1.0e-7

def sum_natural_squares(N):
    """
    Calculates the sum of the squares of all integers upto, and including, N.
    """
    # Returns None if the argument passed to this function cannot be converted into an integer.
    try:
        N = int(N)
    except(ValueError):
        return None
    if N > 0:
        sum = 0
        for i in range(N+1):
            sum += i ** 2
        return sum
    # Returns None if the argument passed to this function is 0 or negative.
    else: 
        return None

def approximate_pi():
    """
    Calculates the approximate value of pi using a summation formula.
    The summation formula runs until the value of the next term in the formula is less than EPSILON.
    That term is not included in the summation.
    """
    pi = float()
    n = 0
    # The loop runs until the next term is less than epsilon. That term is not included in the summation.
    while True:
        term = ((-1) ** n)/((2 * n) + 1)
        n += 1
        if abs(term) < EPSILON:
            break
        else:
            pi += term
    pi = pi * 4
    # Returns pi rounded to 10 decimal places
    return round(pi, 10)

def approximate_sin(x):
    """
    Calculates the approximate value of the sine of x (the argument) using a summation formula.
    The summation formula runs until the value of the next term in the formula is less than EPSILON.
    That term is not included in the summation.
    """
    # Returns None if the argument passed to this function cannot be converted into a float.
    try:
        x = float(x)
    except(ValueError):
        return None
    sin_x = float()
    n = 0
    # The loop runs until the next term is less than epsilon. That term is not included in the summation.
    while True:
        term = (((-1) ** n) * (x ** ((2*n)+ 1))) / math.factorial((2*n) + 1)
        n += 1
        if abs(term) < EPSILON:
            break
        else:
            sin_x += term
    # Returns the sine rounded to 10 decimal places.
    return round(sin_x, 10)

def approximate_cos(x):
    """
    Calculates the approximate value of the cosine of x (the argument) using a summation formula.
    The summation formula runs until the value of the next term in the formula is less than EPSILON.
    That term is not included in the summation.
    """
    # Returns None if the argument passed to this function cannot be converted into a float.
    try:
        x = float(x)
    except(ValueError):
        return None
    cos_x = float()
    n = 0
    # The loop runs until the next term is less than epsilon. That term is not included in the summation.
    while True:
        term = (((-1) ** n) * (x ** (2*n))) / math.factorial(2*n)
        n += 1
        if abs(term) < EPSILON:
            break
        else:
            cos_x += term
    # Returns the cosine rounded to 10 decimal places.
    return round(cos_x, 10)

def display_options():
    ''' This function displays the menu of options'''

    MENU = '''\nPlease choose one of the options below:
             A. Display the sum of squares of the first N natural numbers.         
             B. Display the approximate value of Pi.
             C. Display the approximate value of the sine of X.
             D. Display the approximate value of the cosine of X.
             M. Display the menu of options.
             X. Exit from the program.'''
       
    print(MENU)

def print_difference_from_math_module_value(approximate_value, math_module_value):
    """
    Prints the approximate value, the math module value, and the difference between the two.
    This portion was being repeated enough to warrant being implemented as a function.
    All values are printed to 10 decimal places.
    This function returns None.
    """
    difference = abs(approximate_value - math_module_value)
    print("\n\tApproximation: {:.10f}".format(approximate_value))
    print("\tMath module:   {:.10f}".format(math_module_value))
    print("\tdifference:    {:.10f}".format(difference))

def main():
    """
    Displays the options, waits for the user to pick an option, 
    asks for the argument if the option picked requires any, outputs the resuts of that function.
    This whole function is a continuous loop that runs until the user picks the option 'x'.
    The initial display_options() function call is outside of the while loop 
    as the only other time the menu is displayed is when the user inputs a wrong option
    or the option 'm' is picked.
    """
    display_options()
    while True:
        option = input("\n\tEnter option: ").upper()
        if option == "A":
            sum_argument = input("\nEnter N: ")
            # Checks if N is a valid argument or not, and displays an error message if it isn't.
            if sum_natural_squares(sum_argument) is None:
                print("\n\tError: N was not a valid natural number. [{}]".format(sum_argument))
            else:
                print("\n\tThe sum: {}".format(sum_natural_squares(sum_argument)))
        elif option == "B":
            pi_approximation = approximate_pi()
            print_difference_from_math_module_value(pi_approximation, round(math.pi, 10))
        elif option == "C":
            sin_argument = input("\n\tEnter X: ")
            # Checks if X is a valid argument or not, and displays an error message if it isn't.
            if approximate_sin(sin_argument) is None:
                print("\n\tError: X was not a valid float. [{}]".format(sin_argument))
            else:
                sin_approximation = approximate_sin(sin_argument)
                print_difference_from_math_module_value(sin_approximation, round(math.sin(float(sin_argument)), 10))
        elif option == "D":
            cos_argument = input("\n\tEnter X: ")
            # Checks if X is a valid argument or not, and displays an error message if it isn't.
            if approximate_cos(cos_argument) is None:
                print("\n\tError: X was not a valid float. [{}]".format(cos_argument))
            else:
                cos_approximation = approximate_cos(cos_argument)
                print_difference_from_math_module_value(cos_approximation, round(math.cos(float(cos_argument)), 10))
        elif option == "M":
            display_options()
        elif option == "X":
            print("Hope to see you again.")
            break
        else:
            print("\nError:  unrecognized option [{}]".format(option))
            display_options()


if __name__ == "__main__":
    main()
