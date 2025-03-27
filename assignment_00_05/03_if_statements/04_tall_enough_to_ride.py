def tall_enough():
    min_height = 50
    height = int(input("How tall are you? "))

    if height >= min_height:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

tall_enough()