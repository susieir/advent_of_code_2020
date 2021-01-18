import math


def main(file, step_right, step_down):
    # Open file and read into forest
    with open(file, 'r') as fp:
        forest = fp.read()

    # Return width
    width = forest.find("\n")

    # Create a forest with no line breaks
    forest = forest.replace("\n", "")

    # Find height of forest
    height = int(len(forest) / width)

    pos = 0  # Starting position
#    step_right = 3  # Number of horizontal steps
    tree_count = 0  # Initialise empty tree count
    moves = math.floor(height / step_down)

#    for n in range(moves):
    while pos < len(forest):
        if forest[pos] == "#":
            tree_count += 1
        # Check whether move will cross columns
        if 0 < width - (pos % width) <= step_right:
            # If so, add step_right only
            pos = pos + step_right + ((step_down - 1) * width)
        else:
            # Otherwise normal move
            pos = pos + step_right + (step_down * width)
    return tree_count


if __name__ == '__main__':
    a = main('day3.txt', 1, 1)
    b = main('day3.txt', 3, 1)
    c = main('day3.txt', 5, 1)
    d = main('day3.txt', 7, 1)
    e = main('day3.txt', 1, 2)

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

    print(a * b * c * d * e)


#    read_input('day3.txt')
#    travel_through_forest('day3.txt')
