import pandas as pd

def file_to_string_list(filename):
    """Loads a file into a list of strings"""
    with open(filename, "r") as fp:
        return [str(x) for x in fp.read().splitlines()]

    raise Exception


def dissect_string(items):
    """ Dissects each string to component parts: password, character, lower_b, upper_b"""
    list_of_dicts = []  # Initialise empty list
    for item in items:
        dict_of_params = {}  # Initialise empty dict
        dict_of_params['password'] = item[item.find(":") + 1:].strip()  # Extracts all characters to right of ':' and
        # removes spaces
        dict_of_params['character'] = item[item.find(':') - 1: item.find(':')]  # Extracts the single character
        # before the ':'
        dict_of_params['lower_b'] = int(item[: item.find('-')])  # Extracts the number before the '-'
        dict_of_params['upper_b'] = int(item[item.find('-') + 1: item.find(':') - 1])  # Extracts  number between
        # the '-' and character
        list_of_dicts.append(dict_of_params)
    return list_of_dicts


def check_password(password, character, lower_b, upper_b):
    """ For each list checks whether password is compliant"""
    character_counts = 0  # Initialise empty character count
    for letter in password:
        if letter == character:
            character_counts += 1
    if character_counts in range(lower_b, upper_b + 1):
        return 1

    return 0


def main():
    list_of_dicts = dissect_string(file_to_string_list("day2"))  # Create list_of_dicts
    valid_pw_count = 0  # Initialise empty valid password count
    for dict_of_params in list_of_dicts:
        valid_pw_count += check_password(dict_of_params['password'],
                       dict_of_params['character'],
                       dict_of_params['lower_b'],
                       dict_of_params['upper_b'])
#            print(valid_pw_count)
    print(valid_pw_count)
    print(list_of_dicts[1])
    print(check_password("aaaab", "a", 3, 4))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
