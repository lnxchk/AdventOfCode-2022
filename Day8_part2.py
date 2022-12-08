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


def scenic_score(row, col):
    # this_tree = int(trees[row][col])
    north = view_to_the_north(row, col)
    west = view_to_the_west(row, col)
    east = view_to_the_east(row, col)
    south = view_to_the_south(row, col)
    print("{} {} {} {}".format(north, west, east, south))
    my_score = east * west * north * south
    return my_score


def view_to_the_west(row, col):
    this_tree = int(trees[row][col])
    view_count = 0
    col_count = col - 1
    while col_count >= 0:
        if this_tree > int(trees[row][col_count]):
            view_count += 1
        else:
            return view_count + 1
        col_count -= 1
    return view_count


def view_to_the_east(row, col):
    this_tree = int(trees[row][col])
    view_count = 0
    col_count = col + 1
    while col_count < columns_count:
        if this_tree > int(trees[row][col_count]):
            view_count += 1
        else:
            return view_count + 1
        col_count += 1
    return view_count


def view_to_the_north(row, col):
    this_tree = int(trees[row][col])
    view_count = 0
    local_row_count = row - 1
    while local_row_count >= 0:
        if this_tree > int(trees[local_row_count][col]):
            view_count += 1
        else:
            return view_count + 1
        local_row_count -= 1
    return view_count


def view_to_the_south(row, col):
    this_tree = int(trees[row][col])
    view_count = 0
    local_row_count = row + 1
    while local_row_count < row_count:
        if this_tree > int(trees[local_row_count][col]):
            view_count += 1
        else:
            return view_count + 1
        local_row_count += 1
    return view_count


master_row = 1
# master_col = 1
best_view = 0
while master_row < (row_count - 1):
    master_col = 1
    while master_col < (columns_count - 1):
        print("tree at [{},{}]".format(master_row, master_col))
        count = scenic_score(master_row, master_col)
        print("view {} for [{},{}]".format(count, master_row, master_col))
        if count > best_view:
            best_view = count
        master_col += 1
    master_row += 1

print("the most scenic view: {}".format(best_view))
