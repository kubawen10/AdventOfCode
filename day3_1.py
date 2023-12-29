from common.file_reader import read_file
from typing import Tuple

lines = read_file('input/input3.txt')
non_symbol = '1234567890.'

# return (index of first digit, length of a number) or (-1, -1) if no number found
def find_number(line: str, start: int = 0) -> Tuple[int, int]:
    while start < len(line) and not line[start].isdigit():
        start += 1
    
    if start >= len(line):
        return -1, -1
    
    length = 1
    while start + length < len(line) and line[start + length].isdigit():
        length += 1

    return start, length

def is_symbol(c):
    return c not in non_symbol

def has_symbol(row: int, start: int, length: int): 
    if row < 0 or row >= len(lines):
        return False
    
    start = max(0, start)
    end = min(start+length, len(lines[row]))
    for c in lines[row][start : end]:
        if is_symbol(c):
            return True
    return False

def has_adjecent_symbols(row: int, start: int, length: int):
    # check left
    if start != 0 and is_symbol(lines[row][start-1]):
        return True
    
    if start + length < len(lines[row]) and is_symbol(lines[row][start+length]):
        return True
    
    return has_symbol(row - 1, start-1, length + 2) or has_symbol(row + 1, start - 1, length + 2)


def parse_number(line, start, length):
    return int(line[start:start+length])

sum = 0
for row, line in enumerate(lines):
    start, length = find_number(line)
    while start != -1:
        if has_adjecent_symbols(row, start, length):
            sum += parse_number(line, start, length)

        start, length = find_number(line, start + length + 1)

print(sum)



