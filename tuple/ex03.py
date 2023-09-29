"""
Конкурсный отбор
"""
num = int(input())
pipl = [tuple(input().split()) for i in range(num)]
for i in pipl:
    print(*i)
print()

for i in range(num):
    if int(pipl[i][1]) > 3:
        print(*pipl[i])


