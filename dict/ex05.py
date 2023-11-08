d = {
    "1": [".", ",", "?", "!", ":"],
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"],
    "0": [" "]
}
simpl = ".", ",", "?", "!", ":", "A", "B", "C", "D", "E", "F", "G", "H", "I", \
    "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "

word = input().upper()
count = 1
for i in word:
    for key, value in d.items():
        if i in value:
            count = value.index(i) + 1
            print(key*count, end="")
if len(word) == 0:
    print(0)
