#######################################################################################################################
# Advent of code - Day 10
#######################################################################################################################

# Import collections
from collections import Counter

# Read input list and translate into adaptor list
def read_file(file):
    with open(file, 'r') as fp:
        output_list = [int(a) for a in fp.read().splitlines()]
        return output_list

#adaptor_list = read_file('day10.txt')

# Set device tolerance
#device_tol = 3

# Initialise input
#input = 5




def find_adaptor(adaptor_list, input_jolt, device_tol):
    """ Function that returns the lowest rated adaptor from the adaptor list within the input range for a given input"""
    # Initialise list of valid adaptors
    valid_adaptors = []
    # Generate input range
    input_range = [i for i in range(input_jolt + 1, input_jolt + device_tol + 1)]
    # Iterate through adaptor list until empty
    for adaptor in adaptor_list:
        # Return all adaptors in the input list within the relevant range and add to list of valid adaptors
        for i in input_range:
            if adaptor == i:
                valid_adaptors.append(adaptor)
    # Return the lowest rated adaptor
    chosen_adaptor = min(valid_adaptors)
    return chosen_adaptor


def find_jolt_diff(adaptor, input_jolt):
    # Initialise dictionary of jolt differences
    diff_dict = Counter()
    # Calculate the difference between input and lowest rated adaptor
    jolt_diff = adaptor - input_jolt
    return jolt_diff


def main(file, device_tol, device_delta):
    # Initialise input jolt
    input_jolt = 0
    # Initialise jolt difference dictionary
    jolt_diff_dict = Counter()

    # Generate adaptor list
    adaptor_list = read_file(file)

    # Iterate through the adaptor list
    while len(adaptor_list) > 0:
        # Read the find the right adaptor from the adaptor list
        chosen_adaptor = find_adaptor(adaptor_list, input_jolt, device_tol)
        # Find the jolt difference and add it to the dict
        jolt_diff = find_jolt_diff(chosen_adaptor, input_jolt)
        jolt_diff_dict[jolt_diff] += 1
        print("Jolt difference of {}".format(jolt_diff))
        print(jolt_diff_dict)
        # Set input_jolt equal to chosen_adaptor
        input_jolt = chosen_adaptor
        # Remove adaptor from list
        adaptor_list.remove(chosen_adaptor)
        print("{} removed from adaptor list".format(chosen_adaptor))
    device_jolt = input_jolt + device_delta
    jolt_diff = device_jolt - input_jolt
    jolt_diff_dict[jolt_diff] += 1
    return jolt_diff_dict[1] * jolt_diff_dict[3]

if __name__ == '__main__':
    print(main('day10.txt', 3, 3))