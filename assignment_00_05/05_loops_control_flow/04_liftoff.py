import time

def liftoff():
    for num in range(10,0,-1):
        print(num)
        time.sleep(1)

    print("Liftoff!")

liftoff()