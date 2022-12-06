import sys

# read the line of input in
if len(sys.argv) < 2:
    signal_string = input("Enter signal string: ")
    print()
else:
    signal_string = str(sys.argv[1])


def unique_chars(my_string):
    my_list = []
    my_list[:0] = my_string
    retains = [*set(my_list)]
    if len(retains) < len(my_string):
        return False
    else:
        return True


start_read = 0
end_read = 14
while end_read < len(signal_string):
    test_string = signal_string[start_read:end_read]
    print(test_string)
    if unique_chars(test_string):
        print("Unique chars {} at {}".format(test_string, end_read))
        break
    else:
        pass

    start_read += 1
    end_read += 1

