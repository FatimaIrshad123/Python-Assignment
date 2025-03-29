def num_in_stock(fruit):
    stocks = {"apple":2000,"pear":1000}

    for stock in stocks:
        if fruit not in stock:
            print("This fruit is not in stock.")
        else:
            print(f"This fruit is in stock! Here is how many: {stocks[stock]}")
        
def main():
    fruit = input("Enter a fruit: ")
    num_in_stock(fruit)

main()
