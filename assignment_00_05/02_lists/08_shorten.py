MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        new_list = lst.pop()
        print(new_list)

def get_lst():
    lst = []
    element = input("Enter element: ")
    
    while element != "":
        lst.append(element)
        element = input("Enter element: ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)

main()