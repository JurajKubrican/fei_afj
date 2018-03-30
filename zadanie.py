from pathlib import Path
from sys import argv

in_file = argv[1]

if not Path(in_file).is_file():
    raise Exception('¯\_(ツ)_/¯ file not found :/')

with open(in_file) as f:
    content = f.readlines()

content = [x.strip() for x in content]

max_row = int(content[0])
max_col = int(content[1])

inst = content[2]
pos = 0

# HEAD
col = 0
row = 0
print_char = 0
canvas = [[' ' for y in range(max_col)] for x in range(max_row)]


def read_num(instructions, position):
    global print_char
    char = instructions[position]  # fist num
    nums = ''
    while char.isdigit():
        nums += str(char)
        position += 1  # p
        char = instructions[position]  # fist num
    if not nums.isdigit():
        raise Exception('¯\_(ツ)_/¯ expected a number')
    return int(nums), position


# prints char and moves pos
def print_ch(instructions, position):
    global print_char
    print_char, position = read_num(instructions, position)
    return position


# prints char moves pos
def rpt_ch():
    canvas[row][col] = chr(print_char)


def find_end_bracket(instructions, position):
    # print(instructions, position)
    inception_level = 0

    while position < instructions.__len__():
        char = instructions[position]
        if char == '[':
            inception_level += 1
        elif char == ']':
            inception_level -= 1
        position += 1

        if inception_level < 0:
            return position
    raise Exception('¯\_(ツ)_/¯ bracket error')


def do_the_thing(instructions, position):
    global col, row
    while position < instructions.__len__():
        char = instructions[position]
        position += 1
        if char == 'W':
            row -= 1
        elif char == 'S':
            row += 1
        elif char == 'A':
            col -= 1
        elif char == 'D':
            col += 1

        elif char == 'P':
            position = print_ch(instructions, position)
        elif char == 'Z':
            rpt_ch()
        elif char == '[':
            end_pos = find_end_bracket(instructions, position) - 1
            num, position = read_num(instructions, position)
            for i in range(1, num + 1):
                do_the_thing(instructions[position:end_pos + 1], 0)
            position = end_pos + 1
        elif char == ']':
            return position
        else:
            raise Exception('¯\_(ツ)_/¯ bad char error -' + char)
    return position


def print_the_thing():
    for i in range(0, canvas.__len__()):
        print(''.join(canvas[i]))


if do_the_thing(inst, 0) is not inst.__len__():
    raise Exception('¯\_(ツ)_/¯ bad bracket')
else:
    print_the_thing()
