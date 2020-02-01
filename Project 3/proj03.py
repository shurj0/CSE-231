########################################
#   Project 3
#
#   Program is a continuous loop. If 'no' is answered to the last question, the loop breaks and the program quits.
#   Otherwise, the loop continues
#   while True
#       Prompt for inputs
#       Use inputs to evaluate output using the defined functions
#       Print output
#       Ask if user wants to perform another calculation
#           if user answers yes, continue from start of the loop
#           if user answers no, break out of loop and end program
#
########################################

# The locale module is imported and set up. 
# Later in the program, the locale.currency() function is used to convert a float into a string formatted for currency
import locale

locale.setlocale(locale.LC_ALL, '')

def per_credit(resident, level, college, credits):
    # Calculates per credit tuition.
    # Takes advantage of the fact that the tuition for juniors and seniors are the same 
    # in both resident and non-resident categories, and the tuition for freshmen and sophomores
    # are the same in the non-resident category.
    # College of Engineering or Business only makes a difference if level is Junior or Senior
    per_credit_output = 0.0
    if resident:
        if level == "freshman":
            per_credit_output = 482 * credits
        elif level == "sophomore":
            per_credit_output = 494 * credits
        else:
            if college == "engineering" or college == "business":
                per_credit_output = 573 * credits
            else:
                per_credit_output = 555 * credits
    else:
        if level == "freshman" or level == "sophomore":
            per_credit_output = 1325.50 * credits
        else:
            if college == "engineering" or college == "business":
                per_credit_output = 1385.75 * credits
            else:
                per_credit_output = 1366.75 * credits
    return per_credit_output

def flat_rate(resident, level, college):
    # Same as above, for flat rate tuition
    flat_rate_output = float()
    if resident:
        if level == "freshman":
            flat_rate_output = 7230
        elif level == "sophomore":
            flat_rate_output = 7410
        else:
            if college == "engineering" or college == "business":
                flat_rate_output = 8595
            else:
                flat_rate_output = 8325
    else:
        if level == "freshman" or level == "sophomore":
            flat_rate_output = 19883
        else:
            if college == "engineering" or college == "business":
                flat_rate_output = 20786
            else:
                flat_rate_output = 20501
    return flat_rate_output

def calculate_tuition(resident, international, level, college, CMSE, engineering, JMC, credits):
    # Calculates the total tuition by utilizing the previous two functions
    # and adding misc. charges based on criteria
    tuition = 0.0
    if credits < 12:
        tuition += per_credit(resident, level, college, credits)
    elif credits > 18:
        credits_above_flatrate = credits - 18
        tuition += flat_rate(resident, level, college)
        tuition += per_credit(resident, level, college, credits_above_flatrate)
    else:
        tuition += flat_rate(resident, level,college)
    if credits < 4:
        if college == "business":
            tuition += 113
        elif college == "engineering" or engineering == True:
            tuition += 402
        elif college == "health" or college == "sciences":
            tuition += 50
        elif CMSE:
            tuition += 402
        if international:
            tuition += 375
    else:
        if college == "business":
            tuition += 226
        elif college == "engineering" or engineering == True:
            tuition += 670
        elif college == "health" or college == "sciences":
            tuition += 100
        elif CMSE:
            tuition += 670
        if international:
            tuition += 750
    # ASMSU Tax
    tuition += 21
    # FM Radio Tax
    tuition += 3
    # State News Tax
    if credits >= 6: tuition += 5
    # JMC Student Senate Tax
    if JMC: tuition += 7.50
    # return tuition
    return tuition

print("2019 MSU Undergraduate Tuition Calculator.\n")

while True:
    # (Almost) Everything is set to None by default
    international = None
    college = None
    JMC = None
    CMSE = None
    engineering = None
    # Ask for resident status, then store it as a boolean.
    if input("Resident (yes/no): ").lower() == "yes":
        resident = True
    else:
        resident = False
    # If not resident, ask if international, then store it as a boolean.
    if not resident:
        if input("International (yes/no): ").lower() == "yes":
            international = True
        else:
            international = False
    # Ask for level. The loop runs unless a correct level is entered. 
    while True:
        level = input("Level—freshman, sophomore, junior, senior: ").lower()
        if level in "freshman sophomore junior senior":
            break
        else:
            print("Invalid input. Try again.")
    # Ask for college if junior or senior, then store it as a boolean. Invalid inputs are registered as None.
    if level == "junior" or level == "senior":
        college = input("Enter college as business, engineering, health, sciences, or none: ").lower()
        if college not in "business engineering health sciences":
            college = None
    # Ask if CMSE, then store it as a boolean.
    if level == "junior" or level == "senior":
        if input("Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ").lower() == "yes":
            CMSE = True
        else:
            CMSE = False
    # Ask if Engineering if level is freshman or sophomore, then save it as a boolean
    if level == "freshman" or level == "sophomore":
        if input("Are you admitted to the College of Engineering (yes/no): ").lower() == "yes":
            engineering = True
        else:
            engineering = False
    # Ask if James Madison if college is None, then store it as a boolean
    if (not college) and (not engineering):
        if input("Are you in the James Madison College (yes/no): ").lower() == "yes":
            JMC = True
        else:
            JMC = False
    # Ask for credits, but only accept integers above 0.
    # Using the int() function on a string that isnt an integer (i.e. letters or floats) returns ValueError
    # An exception is raised for the ValueError, and the loop continues until a valid credit is entered.
    while True:
        try:
            credits = int(input("Credits: "))
            if credits <= 0:
                print("Invalid input. Try again.")
                continue
            break
        except(ValueError):
            print("Invalid input. Try again.")
            continue
    # Calculate tuition
    tuition_output = calculate_tuition(resident, international, level, college, CMSE, engineering, JMC, credits)
    # Format in dollars
    formatted_output = locale.currency(tuition_output, grouping=True)
    # Print output
    print("Tuition is {}.".format(formatted_output))
    # Prompt for another calculation
    if input("Do you want to do another calculation (yes/no): ").lower() == "yes":
        continue
    else:
        break


    
        


    

    