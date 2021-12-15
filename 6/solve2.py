from pathlib import Path

# globals
NUM_DAYS = 256
INPUT_FILE = 'input.txt'
FISH_GROWTH_RATE = 7
BABY_MATURITY = 9
BABY_GROWTH_DAY_LOOKUP = {i:1 for i in range(BABY_MATURITY)}

# simulate a day for a school of fish and return the number of new fish spawned
def simulateDay(school):
    numNewFish = 0
    for index, fish in enumerate(school):
        fish -= 1
        if 0 > fish:
            fish = FISH_GROWTH_RATE - 1
            numNewFish += 1

        school[index] = fish

    return numNewFish

# starting with a single baby compute how many fish we have after given amount of days and store in lookup dictionary
def simulateBabyGrowth(days):
    baby = [BABY_MATURITY - 1]
    schoolSize = 0

    currDay = 0
    while days > currDay:
        numNewFishes = simulateDay(baby)
        if 0 < numNewFishes:
            schoolSize += computeNumFishFromBaby(days - currDay - 1)
        currDay += 1

    BABY_GROWTH_DAY_LOOKUP[days] = schoolSize + 1

# return number of fish spawned by baby (incl. baby)
def computeNumFishFromBaby(days):
    if days not in BABY_GROWTH_DAY_LOOKUP:
        simulateBabyGrowth(days)
    
    return BABY_GROWTH_DAY_LOOKUP[days]

# main
# goal: simulate lanternfish exponential growth with given initial school of fish
# -------------------------------------------------------------------------------
filePath = Path(__file__).with_name(INPUT_FILE)
with filePath.open('r') as input:
    school = input.readline().split(',')
    school = [int(fish) for fish in school]

    totalSchoolSize = len(school)
    currDay = 0
    while NUM_DAYS > currDay:
        numBabies = simulateDay(school)
        totalSchoolSize += computeNumFishFromBaby(NUM_DAYS - currDay - 1) * numBabies
        currDay += 1

    print('Result: ' + str(totalSchoolSize))
    # print(BABY_GROWTH_DAY_LOOKUP)