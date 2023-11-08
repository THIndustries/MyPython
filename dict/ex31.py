"""Слияние словарей"""
def merge(values):      # values - это список словарей
    newdict = {}
    for item in values:
        for k,v in item.items():
            if k not in newdict:
                newdict[k] = [v]
            else:
                newdict[k].append(v)

    for k, v in newdict.items():
        newdict[k] = set(v)

    return newdict


result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
print(result)




