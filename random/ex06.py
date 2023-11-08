import random
import string

def generate_index():
    latter = string.ascii_uppercase
    return (f"{random.choice(latter)}{random.choice(latter)}{random.randint(0,99)}_"
            f"{random.randint(0,99)}{random.choice(latter)}{random.choice(latter)}")



print(generate_index())