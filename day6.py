def read_inputs(file):
    """ Read inputs file"""
    with open(file, 'r') as fp:
        inputs = fp.read()
    return inputs


def main(file):
    group_inputs = read_inputs(file).split('\n\n')
    print(group_inputs)
    answer_count = 0  # Initialise empty answer count

    # Loop through entries
    for entry in group_inputs:
        # Replace line breaks with space
        entry = entry.replace('\n','')
        answer_list = []  # start a new answer for each group
        for i in range(len(entry)):  # Iterate through characters
            if entry[i] not in answer_list:  # If character isn't in answer list
                answer_list.append(entry[i])  # Add to answer list
        answer_count += len(answer_list)  # Add the length of the answer list to answer count
        print(answer_list)
    return answer_count



if __name__ == '__main__':
    print(main('day6.txt'))