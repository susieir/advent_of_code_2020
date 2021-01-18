def read_program(filename):
    """ Reads program into list format"""
    with open(filename, 'r') as fp:
        program = fp.read()
        i = 0  # Initialise line counter
        result_list = []  # To store instructions
        for line in program.splitlines():
            operation = line[0:3]
            argument = int(line.split(" ")[1])
            result_list.append((i, operation, argument))
            i += 1
        return result_list

# Success function - given a program, decide whether it meets success criteria - i.e. it gets to the end
# It runs the last instruction


def step_program(program, program_counter=-1, acc=0):
    """ Runs a single step of program and returns the next program state """

    instruction = program[program_counter][1]
    arg = program[program_counter][2]

    if instruction == "acc":
        acc = acc + arg
        program_counter += 1

    elif instruction == "jmp":
        program_counter += arg

    elif instruction == "nop":
        program_counter += 1


    state = (program_counter, acc)
    return state



def main():
    """ Executes instructions in result list"""
    program = read_program("day8.txt")
    print(program)
    pc = 0
    acc = 0
    pc_list = []  # Initialise empty list
    while True:
        state = step_program(program, pc, acc)
        print(state)
        pc = state[0]
        acc = state[1]
        if pc not in pc_list:
            pc_list.append(pc)
        else:
            break



if __name__ == '__main__':
    main()

    """
    0: nop +0
    1: acc +1
    2: jmp +4
    3: acc +3
    4: jmp -3
    5: acc -99
    6: acc +1
    7: jmp -4
    8: acc +6
    """