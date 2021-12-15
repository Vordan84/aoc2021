from pathlib import Path

# constants
NUM_DAYS = 80
INPUT_FILE = 'input.txt'

def simulateDay(school):
    numNewFish = 0
    for index, fish in enumerate(school):
        fish -= 1
        if 0 > fish:
            fish = 6
            numNewFish += 1

        school[index] = fish

    return school + [8 for newFish in range(numNewFish)]

# main
# goal: simulate lanternfish exponential growth with given initial school of fish
# FIXME: precalculate growth of added fishes to avoid exponential loop growth :(
# -------------------------------------------------------------------------------
filePath = Path(__file__).with_name(INPUT_FILE)
with filePath.open('r') as input:
    school = input.readline().split(',')
    school = [int(fish) for fish in school]

    currDay = 0
    while NUM_DAYS > currDay:
        school = simulateDay(school)
        currDay += 1

    print('Result: ' + str(len(school)))