import re

# file = open("day4-sample.txt", "r")
file = open("adventOfCode-Day4.txt", "r")
lines = file.readlines()


def in_range(start_1, stop_1, start_2, stop_2):
    # determine if all numbers in range_1 appear in range_2
    # how can number ranges be included in each other?
    # range_1 completely inside range_2:
    if start_2 <= start_1 and stop_2 >= stop_1:
        print("{} is less than or equal to {}".format(start_2, start_1))
        return True
    # range_2 completely inside range_1:
    elif start_1 <= start_2 and stop_1 >= stop_2:
        return True
    else:
        return False

true_count = 0
for line in lines:
    start_1, stop_1, start_2, stop_2 = re.split("[-,]", line)
    print("{} {} | {} {}".format(start_1, stop_1, start_2, stop_2))
    if in_range(int(start_1), int(stop_1), int(start_2), int(stop_2)):
        true_count += 1
        print("True: {}".format(line))
    else:
        print("False: {}".format(line))


print(in_range(9, 73, 72, 74))
print("The True count is: {}".format(true_count))
