def build_query_string(params):
    result = []
    for i in sorted(params):
        result.append(f"{i}={params[i]}")
    return '&'.join(result)

print(build_query_string({'name': 'timur', 'age': 28}))
print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))