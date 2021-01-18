def dissect_string(string):
    """
    dissect a string in the format "first_position-second_position character password"
    """
    parts = string.split()
    first_position, second_position = [int(x) for x in parts[0].split("-")]
    return first_position, second_position, parts[1][0], parts[2]


def check_password(lower, upper, character, password):
    """
    checks whether the character occurs in the specified positions
    """
    if password[lower-1] == character and password[upper-1] == character:
        return 0
    if password[lower-1] == character or password[upper-1] == character:
        return 1
    return 0


def main():
    with open('day2', 'r') as fp:
        count = 0
        for line in fp.read().splitlines():
            if check_password(*dissect_string(line)):
                count += 1

    print(count)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
