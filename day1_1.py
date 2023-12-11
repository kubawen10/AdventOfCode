from common.file_reader import read_file

lines = read_file('input/input1_1.txt')

def get_number(line: str):
    filtered = list(filter(str.isdigit, line))
    return int(filtered[0] + filtered[-1])

print(sum(map(get_number, lines)))