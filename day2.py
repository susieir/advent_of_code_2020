def dissect_string(string):
    """
    dissect a string in the format "lower-upper character password"
    """
    parts = string.split()
    lower, upper = [int(x) for x in parts[0].split("-")]
    return lower, upper, parts[1][0], parts[2]


def check_password(lower, upper, character, password):
    """
    checks whether the number of occurances of character in password is within limits
    """
    return lower <= password.count(character) <= upper


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
