mydict = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}

count = 0
for i in input():
    for k, v in mydict.items():
        if i in v:
            count += k
print(count)


