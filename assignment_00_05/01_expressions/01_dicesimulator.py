import random

def dice_roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total: int = dice1 + dice2
    print("The sum of two dice are: ",total)

def main():
    dice_roll()
    dice_roll()
    dice_roll()

main()