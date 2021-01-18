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

        field_name_list = []  # Initialise empty field name list
        field_name_requirements = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        # Create list of field names
        for field in fields:
            field_name_list.append(field[0:3])
        print(field_name_list)
        # Check if list of field name requirements is a subset of field name list
        if all(x in field_name_list for x in field_name_requirements):
            compliant_passwords += 1
    print(compliant_passwords)

if __name__ == '__main__':
    main('day4.txt')
