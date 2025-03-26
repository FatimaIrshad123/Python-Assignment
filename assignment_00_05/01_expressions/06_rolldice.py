import random

def roll_dice():
    dic1 = random.randint(1,6)
    dic2 = random.randint(1,6)

    total = dic1 + dic2

    print(f"The result of dice 1 is: {dic1}")
    print(f"The result of dice 2 is: {dic2}")
    print(f"The sum of 2 dice is: {total}")

roll_dice()