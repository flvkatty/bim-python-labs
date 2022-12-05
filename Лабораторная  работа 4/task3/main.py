def delete(list_, index=None):
    length = len(list_)

    if index is None:
        index = length - 1

    if length == 0 or not -length <= index < length:
        raise IndexError

    if index < 0:
        index += length

    return list_[:index] + list_[index + 1:]


print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]

