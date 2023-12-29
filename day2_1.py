from common.file_reader import read_file

lines = read_file('input/input2_1.txt')

def is_possible(line: str) -> int:
    game, rest = line.split(': ')

    for toss in rest.split('; '):
        for num_color in toss.split(', '):
            num, color = num_color.split()
            num = int(num)
            if color == 'red' and num > 12:
                return 0
            elif color == 'green' and num > 13:
                return 0
            elif color == 'blue' and num > 14:
                return 0

    return int(game.split()[1])

sum = 0
for line in lines:
    sum += is_possible(line)

print(sum)
