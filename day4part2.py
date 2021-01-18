import re

def check_byr(byr_entry):
    """ Checks whether byr is between 1920 and 2002 inclusive"""
    if 1920 <= int(byr_entry) <= 2002:
        return True


def check_iyr(iyr_entry):
    """ Checks whether iyr is between 2010 and 2020 inclusive"""
    if 2010 <= int(iyr_entry) <= 2020:
        return True


def check_eyr(eyr_entry):
    """ Checks whether eyr is between 2020 and 2030 inclusive"""
    if 2020 <= int(eyr_entry) <= 2030:
        return True

def check_hgt(hgt_entry):
    """ Checks whether hgt entries in cm are between 150 and 193 inclusive,
    or entries in inches are between 59 and 76 inclusive"""
    if hgt_entry[-2:] == 'cm':
        if 150 <= int(hgt_entry[:-2]) <= 193:
            return True
    if hgt_entry[-2:] == 'in':
        if 59 <= int(hgt_entry[:-2]) <= 76:
            return True

def check_hcl(hcl_entry):
    """ Checks whether hcl entries are in HEX color code format"""
    if hcl_entry[0] != '#':
        return False
    if len(hcl_entry) != 7:
        return False
    try:
        int(hcl_entry[1:], 16)
    except ValueError:
        return False
    return True


def check_ecl(ecl_entry):
    """ Checks whether eye color is within specified list"""
    ecl_allowed_values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if ecl_entry in ecl_allowed_values:
        return True
    return False


def check_pid(pid_entry):
    """ Checks whether pid is a nine digit number including leading zeros"""
    if len(pid_entry) == 9:
        try:
            int(pid_entry)
        except ValueError:
            return False
        return True


def main(file):
    # Read in file
    with open(file, 'r') as fp:
        data = fp.read()
#        print(data)

    # Split into entries
    entries = data.split("\n\n")
    entries = [x.replace("\n", " ") for x in entries]
#    print(entries)


    # Split entries into fields
    compliant_passwords = 0  # Initialise count of compliant passwords
    for entry in entries:
        fields = entry.split(" ")
#        print(fields)
        field_entry_dict = {}  # Initialise empty field name dictionary
        field_name_list = []  # Initialise empty field name list
        field_name_requirements = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        # Create list of field names
        for field in fields:
            field_name_list.append(field[0:3])  # Add field names to list
            field_entry_dict[field[0:3]] = field[field.find(":") + 1:]  # Add entries to dict
#        print(field_name_list)
#        print(field_entry_dict)
        if all(x in field_name_list for x in field_name_requirements):
            if check_byr(field_entry_dict['byr']):
                if check_iyr(field_entry_dict['iyr']):
                    if check_eyr(field_entry_dict['eyr']):
                        if check_hgt(field_entry_dict['hgt']):
                            if check_hcl(field_entry_dict['hcl']):
                                if check_ecl(field_entry_dict['ecl']):
                                    if check_pid(field_entry_dict['pid']):
                                        compliant_passwords += 1
    print(compliant_passwords)
        # Check if list of field name requirements is a subset of field name list


#                compliant_passwords += 1
#    print(compliant_passwords)
#        if

        # Check if list of field name requirements is a subset of field name list
#        if all(x in field_name_list for x in field_name_requirements):
#            compliant_passwords += 1
#    print(compliant_passwords)

if __name__ == '__main__':
   print(main('day4.txt'))
#   print(check_hgt('183cm'))
