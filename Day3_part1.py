# include the priorities file
from Priorities import item_priorities

# read the data file into an array
# file = open("day3_sample.txt", "r")
file = open("adventOfCode-Day3.txt", "r")

lines = file.readlines()

# split each line in half
total = 0
for line in lines:
    line = line.strip()
    length = len(line)
    half = int(length / 2)
    first = line[0:half]
    second = line[half:]
    # for each character in the first half, compare to the second half
    for letter in list(first):
        if letter in second:
            total += item_priorities[letter]
            break

print(total)
