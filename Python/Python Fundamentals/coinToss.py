import random

def coinToss():
    # scores = random_num
    print "Starting the program..."
    headCount = 0

    tailCount = 0
    for toss in range(1,5001):
        face = random.randint(0,1)
        if face == 0:
            coin = "head"
            headCount += 1
        elif face == 1:
            coin = "tail"
            tailCount += 1
        h = "head" if headCount == 1 else "heads"
        t = "tail" if tailCount == 1 else "tails"
        print "Attempt #" + str(toss) + ": Throwing a coin... It's a " + coin + "!  ... Got", headCount, h, "and", tailCount, t, "so far"
    print "Ending the program, thank you!"
coinToss()
