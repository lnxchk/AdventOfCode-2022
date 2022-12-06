import re

# file = open("day4-sample.txt", "r")
file = open("adventOfCode-Day4.txt", "r")
lines = file.readlines()


def overlap(start_1, stop_1, start_2, stop_2):
    # determine if the two ranges overlap at all
    # how can they overlap?
    # 1: range_1 completely inside range_2
    if start_2 <= start_1 and stop_2 >= stop_1:
        return True
    # 2: range_2 completely inside range_1:
    elif start_1 <= start_2 and stop_1 >= stop_2:
        return True
    # 3: range_1 starts before start_2 but ends after it and vice versa:
    elif start_1 <= start_2 <= stop_1:
        return True
    elif start_2 <= start_1 <= stop_2:
        return True
    # 4: range_1 starts after start_2 and ends after stop_2
    elif start_1 <= stop_2 <= stop_1:
        return True
    elif start_2 <= stop_1 <= stop_2:
        return True
    else:
        return False

true_count = 0
for line in lines:
    start_1, stop_1, start_2, stop_2 = re.split("[-,]", line)
    if overlap(int(start_1), int(stop_1), int(start_2), int(stop_2)):
        true_count += 1
        print("True: {}".format(line))
    else:
        print("False: {}".format(line))


print("The True count is: {}".format(true_count))
