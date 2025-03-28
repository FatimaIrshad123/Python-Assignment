def fibonacci():
    current_number = 0
    next_number = 1
    max_number = 10000

    while current_number <= max_number:
        term_next_number = current_number + next_number
        current_number = next_number
        next_number = term_next_number
        print(next_number)

fibonacci()