def is_adult(age):
    ADULT_AGE = 25
    if age >= ADULT_AGE:
        return True
    else:
        return False

def main():
    age = int(input("How old is this person?: "))
    print(is_adult(age))

main()