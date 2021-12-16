from pathlib import Path
import statistics

# global
INPUT_FILE = 'input.txt'

# main
# goal: align all crab submarines
# -------------------------------------------------------------------------------
filePath = Path(__file__).with_name(INPUT_FILE)
with filePath.open('r') as input:
    positions = input.readline().split(',')
    positions = [int(pos) for pos in positions]

    median = round(statistics.median(positions))
    fuel = 0
    for pos in positions:
        fuel += abs(pos - median)

    print('Result - Part1: ' + str(fuel))

    # shooting from hip... with brute force... target should be somewhere around mean position
    mean = round(statistics.mean(positions))

    lowestFuel = float('inf')
    for candidate in range(mean - 8, mean + 8):
        fuel = 0.0

        for pos in positions:        
            steps = abs(pos - candidate)
            fuel += (steps * (steps + 1)) / 2 # triangular sequence for costs
        
        if lowestFuel > fuel:
            lowestFuel = fuel

    print('Result - Part2: ' + str(int(lowestFuel)))