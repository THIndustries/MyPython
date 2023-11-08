numbers = [1, 6, 18]

result = {i: [j for j in range(1, i + 1) if i % j == 0] for i in numbers}

print(result)
