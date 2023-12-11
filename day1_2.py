from common.file_reader import read_file
from typing import List

lines = read_file('input/input1_1.txt')

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def get_number(line: str):
    filtered = list(filter(str.isdigit, line))
    return int(filtered[0] + filtered[-1])

def replace_digits(line: str):
    for i, digit in enumerate(digits):
        line = line.replace(digit, digit + str(i+1) + digit)
    return line

def replace_digits2(line: str):
    for i, digit in enumerate(digits):
        line = line.replace(digit, str(i+1))
    return line

print(sum(map(get_number, map(replace_digits, lines))))


for line in lines:
    l1 = replace_digits(line)
    l2 = replace_digits2(line)
    if get_number(l1) != get_number(l2) :
        print(line, l1, l2)
