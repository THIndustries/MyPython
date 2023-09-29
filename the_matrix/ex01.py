# put your python code here

n = int(input())
m = int(input())

myArray = [[input() for j in range(m)]for i in range(n)]
print('\n'.join(' '.join(i)) for i in myArray)

print()

for j in range(m):
    column = [str(myArray[i][j]) for i in range(n)]
    print(" ".join(column))