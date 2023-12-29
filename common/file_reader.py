from typing import List

def read_file(filename) -> List[str]:
    with open(filename) as f:
        lines = f.readlines()
    return list(map(str.strip, lines))