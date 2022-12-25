import json
from typing import List

INPUT_FILE = "input.csv"


def csv_to_list_dict(
        filename: str,
        delimiter=',',
        new_line='\n'
) -> List[dict]:
    def parse_line(_line: str) -> List[str]:
        return _line[: -len(new_line)].split(delimiter)

    with open(filename) as file:
        header = parse_line(file.readline())
        return [dict(zip(header, parse_line(line))) for line in file]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
