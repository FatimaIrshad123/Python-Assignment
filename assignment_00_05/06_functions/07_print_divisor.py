def print_divisors(num):
    for i in range(num):
        divisor = i + 1
        if num % divisor == 0:
            print(f"{divisor}")

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)

main()