def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done:
            return
        print(curr_num)

def done():
    if random.random < DONE_LIKELIHOOD:
        return True
    return False

def main():
    chaotic_counting()
    print("I'm done")

main()