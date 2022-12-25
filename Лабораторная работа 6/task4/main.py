import json
from typing import List

INPUT_FILE = "input.csv"


def csv_to_list_dict(
        filename: str,
        delimiter=',',
        new_line='\n'
) -> List[dict]:
    with open(filename) as file:
        header = file.readline()[: -len(new_line)].split(delimiter)
        return [dict(zip(header, line[: -len(new_line)].split(delimiter))) for line in file]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
