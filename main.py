def saralash(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1]))

dictionary = {'a': 3, 'b': 1, 'c': 2}
print(saralash(dictionary))  # {'b': 1, 'c': 2, 'a': 3}
