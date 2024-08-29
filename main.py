def data_structure_san(data):
    summ = 0
    if isinstance(data, int):
        summ = data + summ
    elif isinstance(data, str):
        summ = len(data) + summ
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            summ = data_structure_san(item) + summ
    elif isinstance(data, dict):
        for key, value in data.items():
            summ = data_structure_san(key) + data_structure_san(value) + summ
    return summ


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = data_structure_san(data_structure)
print(result)
