
import os

def open_file():
    while True:
        try:
            filename_str = input("Input a file name: ")
            file_obj = open(filename_str, "r")
            break
        # Catches all errors, as there are multiple that can happen when opening files.
        # The error that it catches is, however, specified.
        except Exception as e:
            print(e)
    return file_obj

def fp_setup(file_pointer):
    file_pointer.seek(0)
    file_pointer.readline()
    file_pointer.readline()

def get_us_value(fp):
    fp_setup(fp)
    for line in fp:
        if "United States" in line[:25]:
            return float(line[-5:])

def get_min_value_and_state(fp):
    fp_setup(fp)
    min_value = 100.00
    for line in fp:
        state = str(line[:25])
        try:
            percentage = float(line[-5:])
        except(ValueError):
            continue
        if percentage < min_value:
            min_value = percentage
            min_state = state
    return min_state, min_value

def get_max_value_and_state(fp):
    fp_setup(fp)
    max_value = 0.00
    for line in fp:
        state = str(line[:25])
        try:
            percentage = float(line[-5:])
        except(ValueError):
            continue
        if percentage > max_value:
            max_value = percentage
            max_state = state
    return max_state, max_value

def display_herd_immunity(fp):
    print("\nStates with insufficient Measles herd immunity.")
    print("{:<25s}{:>5s}".format("State","Percent"))
    fp_setup(fp)
    for line in fp:
        state = str(line[:25])
        try:
            percentage = float(line[-5:])
        except(ValueError):
            continue
        if percentage < 90.0:
            print("{:<25s}{:>5s}%".format(state, str(percentage)))

def write_herd_immunity(fp):
    file_obj_out = open("herd.txt", "w")
    file_obj_out.write("States with insufficient Measles herd immunity.\n")
    file_obj_out.write("{:<25s}{:>5s}\n".format("State","Percent"))
    fp_setup(fp)
    for line in fp:
        state = str(line[:25])
        try:
            percentage = float(line[-5:])
        except(ValueError):
            continue
        if percentage < 90.0:
            file_obj_out.write("{:<25s}{:>5s}%\n".format(state, str(percentage)))
    file_obj_out.close()

def main():
    file_pointer = open_file()
    print(file_pointer.readline())
    overall = get_us_value(file_pointer)
    min_state, min_value = get_min_value_and_state(file_pointer)
    max_state, max_value = get_max_value_and_state(file_pointer)
    print("Overall US MMR coverage: {}%".format(overall))
    print("State with minimal MMR coverage: {} {}%".format(min_state.rstrip(), min_value))
    print("State with maximum MMR coverage: {} {}%".format(max_state.rstrip(), max_value))
    display_herd_immunity(file_pointer)
    write_herd_immunity(file_pointer)
    file_pointer.close()

if __name__ == "__main__":
    main()