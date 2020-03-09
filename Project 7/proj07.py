import csv
import math

def open_file():
    """
        Opens a file, and returns its file pointer,
        The function is a continous loop, and loop is broken only when a file is opened,
        As a result, the function continously prompts the user for a file
    """
    while True:
        try:
            filename_str = input("Enter filename: ")
            file_obj = open(filename_str, "r")
            break
        # Catches all errors, as there are multiple that can happen when opening files.
        except Exception:
            print("File not found! Please try again!")
    return file_obj

def calc_multipliers():
    return [ 1 / math.sqrt(n * (n - 1)) for n in range(2, 61) ]

def calc_priorities(state, population, list_of_multipliers):
    return [ (int(population * multiplier), state) for multiplier in list_of_multipliers]

def read_file_make_priorities(fp, modifiers):
    reader = csv.reader(fp)

    # Skips the header.
    next(reader, None)

    # Make a master list so we don't have to use the reader anymore
    # The master list is a list of lists where each list is in the form [state, population]
    # State name is formatted to remove the extra quotes, population is converted to an integer
    # PR and DC are skipped 
    master_list = [[state[1].replace("\"", ""), int(state[2])] for state in reader if (state[1] != "Puerto Rico") and (state[1] != "District of Columbia")]

    # Initialize the state list, and sort it
    state_reps = sorted([[state[0], 1] for state in master_list])

    # Make a list of priority tuples
    priorities = []
    for state in master_list:
        for state_priorities in calc_priorities(state[0], state[1], modifiers):
            priorities.append(state_priorities)

    # Sort the list 
    priorities = sorted(priorities, reverse=True)

    # Get first 385 items only
    priorities = priorities[:386]

    return state_reps, priorities

def add_to_state(state, list_of_states):
    for item in list_of_states:
        if item[0] == state:
            item[1] += 1

def display(list_of_states):
    print("\nState          Representatives")
    for state in list_of_states:
        print("{:<15s}{:>4d}".format(state[0], state[1]))

def main():
    list_of_multipliers = calc_multipliers()
    fp = open_file()
    state_reps, priorities = read_file_make_priorities(fp, list_of_multipliers)
    for state in priorities:
        add_to_state(state[1], state_reps)
    display(state_reps)

if __name__ == "__main__":
    main()