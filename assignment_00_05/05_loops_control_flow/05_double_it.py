def double():
    user_num = int(input("Enter number to double: "))
    max_num = 100

    while user_num < max_num:
        user_num = user_num * 2
        print(user_num)

double()