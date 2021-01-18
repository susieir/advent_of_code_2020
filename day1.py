def file_to_number_list(filename):

    with open(filename, "r") as fp:
        return [int(x) for x in fp.read().splitlines()]

    raise Exception


def find_pair_sum(numbers, sum):
    for i in numbers:
        for j in numbers:
            if i + j == sum:
                return i*j


def find_triple_sum(numbers, sum):
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == sum:
                    return i * j * k




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(find_pair_sum(file_to_number_list("day1.txt"), 2020))
    print(find_triple_sum(file_to_number_list("day1.txt"), 2020))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
