from random import sample

def get_unique_list_numbers(start: int, stop: int, size: int) -> list[int]:
    if stop < start:
        raise ValueError("Конец диапазона должен быть строго больше начала")
    if size > stop - start + 1:
        raise ValueError("Размер выборки должен быть не больше чем размер диапазона")

    return sample(range(start, stop + 1), size)


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))