import math


def find_seat_row(seat_name):
    """ Determines the seat row from the seat name"""
    rows = 128
    min_row = 0
    max_row = 127
    for i in range(7):
        if seat_name[i] == 'F':
            seat_row_range = (min_row, min_row + math.floor((rows / 2) - 1))
            rows = seat_row_range[1] - seat_row_range[0] + 1
            min_row = seat_row_range[0]
            max_row = seat_row_range[1]
        if seat_name[i] == 'B':
            seat_row_range = (max_row + 1 - math.floor(rows / 2), max_row)
            rows = seat_row_range[1] - seat_row_range[0] + 1
            min_row = seat_row_range[0]
            max_row = seat_row_range[1]
    seat_row = seat_row_range[0]
    return seat_row


def find_seat_col(seat_name):
    """ Determines the seat column from the seat name"""
    cols = 8
    min_col = 0
    max_col = 7
    seat_col_str = seat_name[-3:]

    # Cycles through last three letters of seat name
    for i in range(3):
        if seat_col_str[i] == 'L':
            seat_col_range = (min_col, min_col + math.floor((cols / 2) - 1))
            cols = seat_col_range[1] - seat_col_range[0] + 1
            min_col = seat_col_range[0]
            max_col = seat_col_range[1]
        if seat_col_str[i] == 'R':
            seat_col_range = (max_col + 1 - math.floor(cols / 2), max_col)
            cols = seat_col_range[1] - seat_col_range[0] + 1
            min_col = seat_col_range[0]
            max_col = seat_col_range[1]
    seat_col = seat_col_range[0]
    return seat_col


def find_seat_id(seat_name):
    """ For a given seat row and column, return seat ID"""
    seat_id = (find_seat_row(seat_name) * 8) + find_seat_col(seat_name)
    return seat_id


def seat_name_list(file):
    # Read in file to generate seat_name_list
    with open(file, 'r') as fp:
        file_output = fp.read().split('\n')
        return file_output


def main(file):
    """ For a list of seat names, determine the maximum seat index"""
    seat_names = seat_name_list(file)
    seat_id_list = []  # Initialise empty list of seat_ids
    for seat in seat_names:
        seat_id_list.append(find_seat_id(seat))
    seat_list = sorted(seat_id_list)
    for i in range(len(seat_list)):
        delta = seat_list[i+1] - seat_list[i]
        if delta > 1:
            return int((seat_list[i+1] + seat_list[i]) / 2)

#    return max(seat_id_list)


if __name__ == '__main__':
    print(main('day5.txt'))
