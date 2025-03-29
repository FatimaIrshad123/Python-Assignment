def print_ones_digit(num):
    ans = num % 10
    print(f"The ones digit is {ans}")

def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)

main()