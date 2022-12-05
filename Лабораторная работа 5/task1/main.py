from pprint import pprint

result = [
    {
        'dec': num,
        'bin': bin(num),
        'hex': hex(num),
        'oct': oct(num)
    }
    for num in range(0, 16)
]

pprint(result)