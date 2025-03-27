def get_last_element(lst):
    print(lst[-1])

def get_lst():
    lst = []
    element = input("Enter element: ")
    
    while element != "":
        lst.append(element)
        element = input("Enter element: ")
    return lst

def main():
    lst = get_lst()
    get_last_element(lst)

main()