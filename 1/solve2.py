from pathlib import Path

INPUT_FILE = 'input.txt'

filePath = Path(__file__).with_name(INPUT_FILE)
with filePath.open('r') as input:
    lines = input.readlines()

    lastSum = int(lines[0]) + int(lines[1]) + int(lines[2])
    currSum = lastSum
    numIncrements = 0

    for index, line in enumerate(lines):
        if len(lines) > index + 2:
            currSum = int(lines[index]) + int(lines[index + 1]) + int(lines[index + 2])
            if lastSum < currSum :
                numIncrements += 1
            lastSum = currSum

    print(numIncrements)
