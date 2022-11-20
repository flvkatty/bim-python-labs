list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

last_max_pos = 0

for pos, curr in enumerate(list_numbers):
    if curr >= list_numbers[last_max_pos]:
        last_max_pos = pos

list_numbers[last_max_pos], list_numbers[-1] = list_numbers[-1], list_numbers[last_max_pos]

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
