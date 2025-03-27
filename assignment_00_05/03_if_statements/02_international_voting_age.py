def voting_age():
    age = int(input("How old are you? "))
    peturksbouipo = 16
    stanlau = 25
    mayengua = 48

    if age >= peturksbouipo:
        print(f"You can vote in Peturksbouipo where the voting age is 16.")

    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is 16.")

    if age >= stanlau:
        print(f"You can vote in Stanlau where the voting age is 25.")

    else:
        print(f"You cannot vote in Stanlau where the voting age is 25.")

    if age >= mayengua:
        print(f"You can vote in Mayengua where the voting age is 48.")

    else:
        print(f"You cannot vote in Mayengua where the voting age is 48.")

voting_age()