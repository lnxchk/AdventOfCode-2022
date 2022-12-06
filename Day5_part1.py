import re
# file = open("day5-sample.txt", "r")
file = open("adventOfCode-Day5.txt", "r")
lines = file.readlines()


def move_box(from_stack, to_stack):
    box_to_move = stacks[from_stack].pop(0)
    stacks[to_stack].insert(0, box_to_move)


stacks = {}
num_stacks = 9
j = 0
while j <= num_stacks:
    stacks[j] = []
    j += 1

moves_start = 0
# read in the stacks
for line in lines:

    line = line.strip("\n")
    # num_stacks = int((len(line) + 1) / 4)
    i = 0
    if len(line) > 0:
        # print("{} length {}".format(line, len(line)))
        while i < num_stacks:
            start = (i * 4)
            stop = start + 3
            # print("{} : {}".format(start, stop))
            box = line[start:stop]
            # print("{}:{} - {}".format(start, stop, box))
            if "[" in box:
                # print("this is a box: {} in stack {}".format(box, i+1))
                stacks[i+1].append(box)
            # else:
                # print("no box")
            i += 1
        moves_start += 1
    else:
        break


for move_line in lines[moves_start:]:
    # print(move_line)
    m = re.match("move (.+) from (.+) to (.+)", move_line)
    if m:
        num_boxes = int(m.group(1))
        from_stack = int(m.group(2))
        to_stack = int(m.group(3))
        # print("move {} from {} to {}".format(num_boxes, from_stack, to_stack))
        to_move = 1
        while to_move <= int(num_boxes):
            move_box(from_stack, to_stack)
            to_move += 1


print(stacks)

list_out = 1
print(stacks[1][0])
print(num_stacks)
while list_out <= num_stacks:
    print(stacks[list_out][0])
    list_out += 1
