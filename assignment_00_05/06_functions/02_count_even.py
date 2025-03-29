def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1

    print(count)

def list_of_int():
    user_input = input("Enter an integer or press enter to stop: ")
    lst = []

    while user_input != "":
        lst.append(int(user_input))
        user_input = input("Enter an integer or press enter to stop: ")

    return lst

def main():
    lst = list_of_int()
    count_even(lst)

main()