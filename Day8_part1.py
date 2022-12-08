# file = open("day8-sample.txt", "r")
file = open("adventOfCode-Day8.txt", "r")
lines = file.readlines()

trees = {}
row_count = 0
for line in lines:
    trees[row_count] = [*line.strip()]
    row_count += 1

columns_count = int(len(lines[0])) - 1
print("there are {} rows and {} cols".format(row_count, columns_count))
# print(trees)
# compute the outer box - all edge trees will be visible
north = len(lines[0].strip())
east = len(lines) - 1
south = len(lines[-1].strip()) - 1
west = len(lines) - 2
outside = north + south + east + west
visible_trees = outside
print("outside visible trees: {}".format(visible_trees))
# for a tree to be visible from a particular direction, it
# must be the tallest tree in that direction between itself
# and the edge.


def is_it_tallest(row, col):
    # this_tree = int(trees[row][col])
    if tallest_to_the_east(row, col):
        return 1
    elif tallest_to_the_west(row, col):
        return 1
    elif tallest_to_the_north(row, col):
        return 1
    elif tallest_to_the_south(row, col):
        return 1
    else:
        return 0


def tallest_to_the_west(row, col):
    this_tree = int(trees[row][col])
    col_count = 0
    while col_count < col:
        if this_tree <= int(trees[row][col_count]):
            return False
        col_count += 1
    return True


def tallest_to_the_east(row, col):
    this_tree = int(trees[row][col])
    col_count = col + 1
    while col_count < columns_count:
        if this_tree <= int(trees[row][col_count]):
            return False
        col_count += 1
    return True


def tallest_to_the_north(row, col):
    this_tree = int(trees[row][col])
    local_row_count = 0
    while local_row_count < row:
        if this_tree <= int(trees[local_row_count][col]):
            return False
        local_row_count += 1
    return True


def tallest_to_the_south(row, col):
    this_tree = int(trees[row][col])
    local_row_count = row + 1
    while local_row_count < row_count:
        if this_tree <= int(trees[local_row_count][col]):
            return False
        local_row_count += 1
    return True


master_row = 1
# master_col = 1
while master_row < (row_count - 1):
    master_col = 1
    while master_col < (columns_count - 1):
        print("tree at [{},{}]".format(master_row, master_col))
        count = is_it_tallest(master_row, master_col)
        print("adding {} for [{},{}]".format(count, master_row, master_col))
        visible_trees += count
        master_col += 1
    master_row += 1

print("total visible trees: {}".format(visible_trees))
