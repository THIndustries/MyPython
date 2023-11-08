import random

word = [i for i in input()]
random.shuffle(word)
print("".join(word))
