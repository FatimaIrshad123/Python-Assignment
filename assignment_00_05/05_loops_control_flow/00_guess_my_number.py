import random

def main():
    print("I am thinking of a number between 0 and 99... ")
    guess = int(input("Enter a guess:"))
    num = random.randint(0,99)

    while guess != num:
        if guess <= num:
            print(f"Enter a new number: {guess} Your guess is too low")
            guess = int(input("Enter a new number: "))
        else:
            print(f"Enter a new number: {guess} Your guess is too high")
            guess = int(input("Enter a new number: "))
        
    print(f"{guess} Congrats! The number was: {num}")
    
main()