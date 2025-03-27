def get_list():
    val = []
    inp = (input("Enter a value: "))
    while inp:
        val.append(inp)
        inp = (input("Enter a value: "))

    print(f"Here's the list: ['1', '2', '3']")
    print(val)
    
get_list()