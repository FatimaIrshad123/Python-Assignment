import math

def pythagorean_theorm():
    length_AB = int(input("Enter the length of AB: "))
    length_AC = int(input("Enter the length of AC: "))
    BC = length_AB ** 2 + length_AC ** 2
    print(BC)
    print(math.sqrt(BC))  

pythagorean_theorm()