"""
    Project 6 

    This program is used to parse data from the NHL in a CSV file format 
    and return useful information in a readable format.

    The csv file is opened, the data is parsed using various functions,
    and the main loop is used to output the information.
"""

import csv

def open_file():
    """
        Opens a file, and returns its file pointer,
        The function is a continous loop, and loop is broken only when a file is opened,
        As a resut, the function continously prompts the user for a file
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

def read_file(fp):
    """
        Creates an empty master list,
        Iterates through the csv file passed as a parameter (Skipping the header),
        Appends each line (in list form) to the master list,
        Returns the master list.
    """
    master_list = []
    reader = csv.reader(fp)
    # Skips the header.
    next(reader, None)
    for line_list in reader:
        master_list.append(line_list)
    return master_list

def shoots_left_right(master_list):
    """
        Counts the number of left and right shooters, and returns them in that order
    """
    left = 0
    right = 0
    for player in master_list:
        if player[1] == "L":
            left += 1
        else:
            right += 1
    return left, right

def position(master_list):
    """
        Counts the number of players in each position,
        Returns them in the order left, right, center, defense
    """
    left = 0
    right = 0 
    center = 0 
    defense = 0
    for player in master_list:
        # Create a pos variable because we have to use it more than once
        pos = player[2]
        if pos == "L":
            left += 1 
        elif pos == "R":
            right += 1
        elif pos == "C":
            center += 1
        else:
            defense += 1
    return left, right, center, defense

def off_side_shooter(master_list):
    """
        Counts the number of players who are off side shooters,
        Returns them in the order of left-wing-shooting-right, and right-wing-shooting-left
    """
    left_pos_right_shoot = 0
    right_pos_left_shoot = 0
    for player in master_list:
        # Create variables for position and shooting because we have to use them more than once
        shoot = player[1]
        pos = player[2]
        if pos == "L":
            if pos == shoot:
                continue
            else:
                left_pos_right_shoot += 1
        elif pos == "R":
            if pos == shoot:
                continue
            else:
                right_pos_left_shoot += 1
        # If position is not L or R, the player can't be an offside shooter
        else:
            continue 
    return left_pos_right_shoot, right_pos_left_shoot

# The next three functions are single lines because it was a challenge, so sorry for them being not very readable

def points_per_game(master_list):
    """
        Iterates through every player in master_list passed as a parameter,
        Constructs a tuple of points per game (converted to float), player name, player position,
        Makes a list of those tuples,
        Sorts the list in descending order (i.e. reverse = True)
        Returns the first 10 items from the sorted list
    """
    return sorted([(float(player[18]), player[0], player[2]) for player in master_list], reverse = True)[:10]

def games_played(master_list):
    """
        Iterates through every player in master_list passed as a parameter,
        Constructs a tuple of games played (converted to int, removing commas) and player name,
        Makes a list of those tuples,
        Sorts the list in descending order (i.e. reverse = True)
        Returns the first 10 items from the sorted list
    """
    return sorted([(int(player[3].replace(",","")), player[0]) for player in master_list], reverse = True)[:10]

def shots_taken(master_list):
    """
        Iterates through every player in master_list passed as a parameter,
        Constructs a tuple of shots taken (converted to int, removing commas) and player name,
        Unless the shots taken value doesn't exist (i.e. has a string "--"), in which case that player is skipped
        Makes a list of those tuples,
        Sorts the list in descending order (i.e. reverse = True)
        Returns the first 10 items from the sorted list
    """
    return sorted([(int(player[9].replace(",","")), player[0]) for player in master_list if player[9] != "--"], reverse = True)[:10]

def main():
    """
        Opens the file and stores the file pointer as fp,
        Reads the file and stores the list of list in master_list,
        Prints out the data in the required format
    """
    fp = open_file()
    master_list = read_file(fp)
    # Mimir expects an additional newline here
    print("\n")

    # --- Shooting --- #

    print("{:^10s}".format("\nShooting"))
    # The function output, which is a tuple, is passed directly into the .format() method using the "*" prefix
    # This breaks down the tuple into indivitual arguments that the method can parse
    print("left:      {:4d}\nright:     {:4d}".format(*shoots_left_right(master_list))) 

    # --- Position --- #

    print("{:^12s}".format("\nPosition"))
    print("left:    {:4d}\nright:   {:4d}\ncenter:  {:4d}\ndefense: {:4d}".format(*position(master_list))) # Same thing done here

    # --- Off side shooter --- #

    print("{:^24s}".format("\nOff-side Shooter"))
    print("left-wing shooting right: {:4d}\nright-wing shooting left: {:4d}".format(*off_side_shooter(master_list))) # And here

    # --- Top Ten Points-Per-Game --- #

    print("{:^36s}".format("\nTop Ten Points-Per-Game"))
    print("{:<20s}{:>8s}{:>16s}".format("Player", "Position", "Points Per Game"))
    for player in points_per_game(master_list):
        # The print order is different from the order in which the function returns, so indexing must be done
        print("{:<20s}{:>8s}{:>16.2f}".format(player[1], player[2], player[0]))

    # --- Top Ten Games Played --- #

    print("{:^36s}".format("\nTop Ten Games-Played"))
    print("{:<20s}{:>16s}".format("Player", "Games Played"))
    for player in games_played(master_list):
        # The print order is different from the order in which the function returns, so indexing must be done
        print("{:<20s}{:>16,d}".format(player[1], player[0]))

    # --- Top Ten Shots Taken --- #

    print("{:^36s}".format("\nTop Ten Shots-Taken"))
    print("{:<20s}{:>16s}".format("Player", "Shots Taken"))
    for player in shots_taken(master_list):
        # The print order is different from the order in which the function returns, so indexing must be done
        print("{:<20s}{:>16,d}".format(player[1], player[0]))

if __name__ == "__main__":
    main()