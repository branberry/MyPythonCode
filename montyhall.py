import random

GAME_LENGTH = 3


def montyhall(door,switch):
    correct = 0
    incorrect = 0
    for i in range(100000):
        game = [False,False,False]
        key = random.randint(0,2)
        game[key] = True
        if game[door] == True:
            correct += 1
        else:
            incorrect += 1

        if switch == True:
            newDoor = 0
            removed = 0
            for v in range(3):
                if v != key and door != v:
                    game.remove(game)
                    removed = v
                    break

            if door == 0 and removed != 1:
                newDoor = door + 1
            elif door == 0 and removed != 2:
                newDoor = 2
            elif door == 1 and removed != door - 1:
                newDoor = door - 1
            elif door == 1 and removed != door + 1:
                newDoor = door + 1

            if game[newDoor] == True:
                correct += 1
            elif game[newDoor] == False:
                incorrect += 1

    print("correct: ",correct)
    print("incorrect: ",incorrect)
    total = correct + incorrect
    percent = correct/total
    print(percent)

montyhall(1,False)
montyhall(1,True)
