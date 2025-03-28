def pop_up_shop():
    fruits = {"apple":12, "mango":10}
    total = 0
    for fruit in fruits:
        item = int(input(f"How many {fruit} do you want?:"))
        price = item*fruits[fruit]
        total += price
    print(f"Your total is ${total}")

pop_up_shop()