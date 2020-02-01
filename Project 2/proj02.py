####################################
#
#   Project 2
#
#   Algorithm
#       Ask to continue
#           Gather information about the rental and check validity
#           Perform calculations
#           Output results
#
####################################

import math

BANNER = "\nWelcome to car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BDW) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)" 

print(BANNER)

prompt_answer = input("\nWould you like to continue (Y/N)? ")
while prompt_answer == "Y":
    # ~~~ Customer Code Loop ~~~ #
    # This loop ensures that the user cannot proceed without inputting a valid customer code first. 
    # The loop ends only when a valid customer code is entered.
    customer_code = ""                                                    
    while not(customer_code == "B" or customer_code == "D" or customer_code == "W"):
        customer_code = input("\nCustomer code (BDW): ")
        if not(customer_code == "B" or customer_code == "D" or customer_code == "W"):
            print("\n\t*** Invalid customer code. Try again. ***")
    # ~~~ Other Inputs ~~~ # 
    number_of_days = int(input("\nNumber of days: "))
    odometer_start = int(input("Odometer reading at the start: "))
    odometer_end = int(input("Odometer reading at the end:   "))
    # ~~~ Calculations ~~~ #
    # This part ensures correct calculation in case of odometer overflow
    # In such a case, the number of miles is =
    # (Odometer end reading) + (Number of miles till overflow from the odometer start reading)
    if odometer_end < odometer_start:
        miles = abs(odometer_end + (1000000 - odometer_start)) / 10
    else:
        miles = abs(odometer_end - odometer_start) / 10
    # B 
    if customer_code == "B":
        amount_due = (40 * number_of_days) + (0.25 * miles)
    # D
    elif customer_code == "D":
        chargable_miles = miles - (number_of_days * 100)
        if chargable_miles <= 0: chargable_miles = 0
        amount_due = (60 * number_of_days) + (0.25 * chargable_miles)
    # W
    elif customer_code == "W":
        # Rounds up the number of weeks since a partial week is considered a full week for the purposes of this program
        number_of_weeks = math.ceil(number_of_days / 7)
        amount_due = number_of_weeks * 190.00
        if (miles / number_of_weeks) >= 900 and (miles / number_of_weeks) < 1500:
            amount_due = amount_due + (100.00 * number_of_weeks)
        elif (miles / number_of_weeks) > 1500:
            amount_due = amount_due + (200.00 * number_of_weeks) + (((((miles / number_of_weeks) - 1500.00) * number_of_weeks) * 0.25))
    # ~~ Output ~~ #
    print("\nCustomer summary:")
    print("\tclassification code: {}".format(customer_code))
    print("\trental period (days): {}".format(number_of_days))
    print("\todometer reading at start: {}".format(odometer_start))
    print("\todometer reading at end:   {}".format(odometer_end))
    print("\tnumber of miles driven:  {}".format(miles))
    print("\tamount due: $ {}".format(round(amount_due, 2)))
    # ~~ Loop continue prompt ~~ #
    prompt_answer = input("\nWould you like to continue (Y/N)? ")
    if prompt_answer == "Y":
        continue
    else:
        break 
# The print statement lies outside of the loop in order to display the message if the user answers "N" to the first prompt.
print("Thank you for your loyalty.")