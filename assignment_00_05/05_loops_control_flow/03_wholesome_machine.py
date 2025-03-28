def wholesome():
    affirmation = "I am capable of doing anything I put my mind to."
    user_input = input(f"Please type the following affirmation: {affirmation}")

    while user_input != affirmation:
        print("Hmmm That was not the affirmation.")

        print("Please type the following affirmation: " + affirmation)
        user_input = input()

    print("That's right! :)")

wholesome()