def leap_year():
    year: int = int(input("Enter Year: "))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"That's a leap year!")
            else:
                print(f"That's not a leap year!")

        else:
            print(f"That's a leap year!")
    else:
        print(f"That's not a leap year!")

leap_year()