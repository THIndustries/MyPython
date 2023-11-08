"""Опасный вирус"""
mydict1 = {}
mydict2 = {
    'W': 'write',
    'R': 'read',
    'X': 'execute'
}
for i in range(int(input())):
    text = input().split()
    for j in text[1:]:
        mydict1[text[0]] += mydict2[j]
print(mydict1)

for i in range(int(input())):
    text2 = input().split()
    if text2[1] in mydict1.get(text2[0]):
        print("OK")
    else:
        print("Access denied")


#___________________________________________________________________

ACTION_PERMISSION = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}

file_permissions = {}
for i in range(int(input())):
    file, *permissions = input().split()
    file_permissions[file] = set(permissions)

for i in range(int(input())):
    action, file = input().split()
    if ACTION_PERMISSION[action] in file_permissions[file]:
        print('OK')
    else:
        print('Access denied')
