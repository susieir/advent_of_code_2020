def main(file):
    # Open file and read into forest
    with open(file, 'r') as fp:
        forest = fp.read()

    # Return width
    width = forest.find("\n")

    # Create a forest with no line breaks
    forest = forest.replace("\n","")

    # Find height of forest
    height = int(len(forest) / width)

    pos = 0  # Starting position
    step = 3  # Number of horizontal steps
    tree_count = 0  # Initalise empty tree count

    for n in range(height):
    #while pos < len(forest):
        if forest[pos] == "#":
            tree_count += 1
        # Check whether move will cross columns
        #if 0 < (width - ((pos + width) % width)) < 3:
        if 0 < width - (pos % width) <= 3:
            # If so, add step only
            pos = pos + step
            #if forest[pos] == "#":
            #    tree_count += 1
    #        print(pos)
        else:
            # Otherwise normal move
            pos = pos + step + width
            #if forest[pos] == "#":
            #    tree_count += 1
    print(width)
    print(len(forest))
    print(pos)
    print(tree_count)
    #        print(pos)


if __name__ == '__main__':
    main('day3.txt')
#    read_input('day3.txt')
#    travel_through_forest('day3.txt')
