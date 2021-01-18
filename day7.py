def read_inputs(file):
    """ Read inputs file"""
    with open(file, 'r') as fp:
        inputs = fp.read()
    return inputs.splitlines()  # \n or \r\n
#    inputs = read_inputs(file)
#    for i in range(len(inputs)):
#    word_list = inputs[i].split(" ")


def parse_bag_line(line):
    """
    given a line like: 'light red bags contain 1 bright white bag, 2 muted yellow bags.'
    return a tuple (main bag, [containee bags])
    """
    # step 1 - clean up punctuation in line and replace all instance of 'bag' with 'bags'
    line = line.replace(".", "")
    line = line.replace(",", "")
    line = line.replace("bags", "bag")
    # step 2 - split line into words
    word_list = line.split(" ")
    # step 3 - read main bag
    main_bag = word_list[0] + " " + word_list[1]
    i = 4
    results = []
    while i < len(word_list):
        # step 4 - find the next position of the keyword 'bag' or 'bags'
        next_pos = word_list.index('bag', i)
        # step 5 - pick the next bag description and add it to the results list
        results.append(word_list[next_pos - 2] + " " + word_list[next_pos - 1])
        i = next_pos + 1

    return (main_bag, results)


def process_bag_inputs(file, bag):
    """
    open file and loop through all the lines, return a list of container bags that could
    contain 'bag'
    """
    inputs = read_inputs(file)
    bag_dict = {}  # Initialise dictionary of containers and containee bags
    results = []  # Initialise empty results list
    results.append(bag)  # Add bag to empty results list

    # For each line, add the main_bag and sub_bags to a dictionary
    for line in inputs:
        main_bag, sub_bags = parse_bag_line(line)
        for item in sub_bags:
            if item in bag_dict:
                bag_dict[item].append(main_bag)
            else:
                bag_dict[item] = [main_bag]
#        bag_dict[main_bag] = sub_bags
    print(bag_dict)

    start_list = bag_dict[bag]
    for key, values in bag_dict.items():
        if key in start_list:
            if
            start_list.append(values)

    print(start_list)

#        for value in bag_dict.items():
#            if value in results:
#                results.append(key)





if __name__ == '__main__':
    print(process_bag_inputs('day7.txt', 'shiny gold'))
#    print(parse_bag_line('light red bags contain 1 bright white bag, 2 muted yellow bags.'))
#    print(inside_bag_colors('day7.txt'))