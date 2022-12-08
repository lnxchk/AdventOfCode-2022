# import re
# open the file
# file = open('day7-sample.txt', 'r')
file = open("adventOfCode-Day7.txt", 'r')
lines = file.readlines()


def walk_through(parent_dir, some_lines):
    local_total = 0
    while some_lines:
        line = some_lines.pop(0).strip()
        if line == "$ cd ..":
            dirs[parent_dir] = local_total
            # print(local_total)
            return local_total
        elif line.startswith("$ cd"):
            this_dir = line[5:]
            if this_dir == "/":
                this_dir = "root"
            else:
                this_dir = parent_dir + "_" + this_dir
            print("going to dir {}".format(this_dir))
            return_total = walk_through(this_dir, some_lines)
            print("returned {} from dir {}".format(return_total, this_dir))
            local_total = local_total + return_total
        elif line[0].isdigit():
            # print("this line is a file with size {}".format(line))
            file_size, file_name = line.split(" ")
            print("adding {} to local_total".format(file_size))
            local_total += int(file_size)
        else:
            # pass
            print("ignoring: {}".format(line))

    dirs[parent_dir] = local_total
    return local_total

dirs = {}
files = {}
my_dir = ""
throw_away = lines.pop(0)
root_total = walk_through("root", lines)
dirs["root"] = root_total
print(dirs)
print("there are {} directories".format(len(dirs)))
global_total = 0
for this_dir in dirs:
    if dirs[this_dir] < 100000:
        print("adding {} for {}".format(dirs[this_dir], this_dir))
        global_total += dirs[this_dir]


print(global_total)
