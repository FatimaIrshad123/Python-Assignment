def add_three_copies(lists, data):
    lists.append(data)
    
def main():
    lists = []
    print(f"List before: {lists}")
    data = input("Enter a message to copy: ")
    add_three_copies(lists,data)
    add_three_copies(lists,data)
    add_three_copies(lists,data)
    print(f"List after: {lists}")

main()