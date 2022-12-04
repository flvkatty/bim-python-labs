def delete(list_, index=-1):
    if index == -1 or index == len(list_) - 1:
        return list_[:index]
    else:
        return list_[:index] + list_[index + 1:]


print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
