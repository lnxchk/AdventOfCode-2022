all_possible_hands = {
	"AX": 3,
	"AY": 4,
	"AZ": 8,
	"BX": 1,
	"BY": 5,
	"BZ": 9,
	"CX": 2,
	"CY": 6,
	"CZ": 7
}


def play_round(this_hand):
	if this_hand in all_possible_hands:
		return all_possible_hands[this_hand]
	else:
		return 0


# file = open("day2_sample.txt", "r")
file = open("adventOfCode-Day2.txt", "r")
total = 0

lines = file.readlines()

for line in lines:
	line = line.strip()
	line = line.replace(" ", "")
	total += play_round(line)


print(total)
file.close()
