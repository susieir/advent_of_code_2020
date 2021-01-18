def read_inputs(file):
    """ Read inputs file"""
    with open(file, 'r') as fp:
        inputs = fp.read()
    return inputs


def main(file):
    group_inputs = read_inputs(file).split('\n\n')  # Breaks into groups
#    print(group_inputs)

    answer_count = 0  # Zero count of intersection length

    # Create a list of answers for a given group
    for group_answer in group_inputs:
        group_answer_list = group_answer.splitlines()
#        print(group_answer_list)

        # Within each group, create a set for each answer
        for i in range(len(group_answer_list)):  # For each answer
            group_answer_list[i] = set(group_answer_list[i])

            current_intersection = group_answer_list[0]  # Create a base set, with the first answer for the group
#            print(group_answer_list)

        # Create set of letters which appear in each answer
        for i in range(1, len(group_answer_list)):
            current_intersection = current_intersection.intersection(group_answer_list[i])
        print(current_intersection)
        # Add the length of the current_intersection to the answer count
        answer_count += (len(current_intersection))
    print(answer_count)


if __name__ == '__main__':
    (main('day6.txt'))