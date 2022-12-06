
from operator import itemgetter

file = open("adventOfCode-Day1.txt", "r")
# file = open("day1_short.txt", "r")
lines = file.readlines()

elves = {} 

elf_count = 0
for line in lines:
	line = line.strip("\n")
	if line != "":
		x = int(line) 
		if elf_count not in elves:
			elves[elf_count] = x
		else:
			elves[elf_count] += x
	else:
		elf_count += 1

# print(elves)

max_value = max(elves.values())
print(max_value)

sort_elves = dict(sorted(elves.items(), key=itemgetter(1), reverse = True)[:3])
print(sort_elves)

total = 0
for elf in sort_elves:
	total += sort_elves[elf]

print(total)

