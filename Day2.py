
their_moves = {
	'A': "rock",
	'B': "paper",
	'C': "scissors"
}

my_moves = {
	'X': "rock",
	'Y': "paper",
	'Z': "scissors"
}

i_win = {
	"CX": 7,
	"AY": 8,
	"BZ": 9
}

they_win = {
	"AZ": 3,
 	"BX": 1,
	"CY": 2 
}
we_draw = {
	"AX": 4,
 	"BY": 5,
	"CZ": 6
}


def play_round(this_hand):
	if this_hand in i_win:
		return i_win[this_hand]
	elif this_hand in they_win:
		return they_win[this_hand]
	elif this_hand in we_draw:
		return we_draw[this_hand]
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
