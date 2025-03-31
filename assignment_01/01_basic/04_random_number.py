import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100
listOfNum = []

def main():
    for i in range(0,10):
      listOfNum.append(random.randint(MIN_VALUE,MAX_VALUE))

    print(listOfNum)
main()