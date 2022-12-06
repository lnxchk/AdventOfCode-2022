# include the priorities file
from Priorities import item_priorities

# read the data file into an array
# file = open("day3_sample.txt", "r")
file = open("adventOfCode-Day3.txt", "r")

lines = file.readlines()
length_of_lines = len(lines)

# split each line in half
total = 0
line_num = 0
while line_num < length_of_lines:
    this_line = lines[line_num].strip()
    # build arrays of the next lines of rucksacks
    next_line = lines[line_num + 1].strip()
    third_line = lines[line_num + 2].strip()

    this_array = list(this_line)

    potentials = []
    for letter in this_array:
        if letter in next_line and letter not in potentials:
            potentials.append(letter)

    for new_letter in potentials:
        if new_letter in third_line:
            total += item_priorities[new_letter]
            break

    print(potentials)

    line_num += 3


print(total)
