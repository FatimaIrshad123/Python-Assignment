def read_phone_numbers():
    phonebook = {}

    while True:
        name = input("Enter a name: ")
        if name == "":
            break

        num = int(input("Enter a number: "))
        phonebook[name] = num
    return phonebook

def print_phonebook(phonebook):
    for name in phonebook:
        print(str(name) + " => " + str(phonebook[name]))

def count_nums(nums_lst):
    num_dict = {}
    for num in nums_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1

    return num_dict

def lookup_number(phonebook):
    while True:
        name = input("Enter a name for lookup: ")
        if name == "":
            break
        elif name not in phonebook:
            print("Name is not in Phonebook")
        else:
            print(phonebook[name])


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_number(phonebook)

main()