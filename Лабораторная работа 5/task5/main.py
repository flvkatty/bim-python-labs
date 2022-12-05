import string
from random import sample

alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits


def get_random_password(n: int = 8) -> str:
    if not 0 < n <= len(alphabet):
        raise ValueError(f"Размер пароля должен быть в диапазоне ({0},{len(alphabet)}]")

    return ''.join(sample(alphabet, n))

print(get_random_password())
