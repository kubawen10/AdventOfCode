from common.file_reader import read_file

lines = read_file('input/input2_1.txt')

def power(line: str) -> int:
    _, rest = line.split(': ')

    min_red = 0
    min_green = 0
    min_blue = 0

    for toss in rest.split('; '):
        for num_color in toss.split(', '):
            num, color = num_color.split()
            num = int(num)
            if color == 'red' and num > min_red:
                min_red = num
            elif color == 'green' and num > min_green:
                min_green = num
            elif color == 'blue' and num > min_blue:
                min_blue = num
    return min_red*min_blue*min_green

sum = 0
for line in lines:
    sum += power(line)
print(sum)