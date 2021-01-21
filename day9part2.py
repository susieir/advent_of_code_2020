""" Advent of code puzzle - Day 9"""

""" Part 1 code"""
def create_input_list(filename):
    """ Reads the input data and stores as a list"""
    with open(filename, 'r') as fp:
        return [int(x) for x in fp.read().splitlines()]


def inspect_check_number(filename, step=5, inc=0):
    """ Function that inspects whether the check number is valid by checking against a list of valid numbers"""
    # Set up the list
    cypher = create_input_list(filename)
    # Find the check number to be inspected
    check_number = cypher[step + inc]

    # Initialise check_list - stores possible valid check_numbers
    check_list = []
    # Loop through the previous numbers
    for i in cypher[inc : step + inc]:
        for j in cypher[inc : step + inc]:
            if i != j:
                check_list.append(i + j)

    # Check if check_number is in check_list
    if check_number in check_list:
        return (check_number, "ok")
    else:
        return (check_number, "test failed")


def find_invalid_num(filename, step = 5):
    """Iterates through each item in cypher"""
    c = 0 # initialise c
    cypher = create_input_list(filename)
    for c in range(len(cypher) - step):
        if inspect_check_number(filename, step, inc = c)[1] == "test failed":
            invalid_num = inspect_check_number(filename, step, inc = c)[0]
            return invalid_num
            break


def main(filename, step):
    # Re-create invalid num
    invalid_num = find_invalid_num(filename, step)
    # Re-create cypher list
    cypher = create_input_list(filename)
    # Loop through contiguous ranges to check for invalid number
    for i in range(len(cypher)):
        for j in range(len(cypher)):
            if sum(cypher[i:j]) == invalid_num:
                if len(cypher[i:j]) != 1:
                    print(sum([min(cypher[i:j]), max(cypher[i:j])]), "contiguous set found")
                    break




# Loop through list to find contiguous range


if __name__ == '__main__':
    print(main('day9.txt', step=25))
