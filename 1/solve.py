from pathlib import Path

INPUT_FILE = 'input.txt'

filePath = Path(__file__).with_name(INPUT_FILE)
with filePath.open('r') as input:
    lines = input.readlines()

    lastLine = int(lines[0])
    numIncrements = 0

    for line in lines:
        if lastLine < int(line) :
            numIncrements += 1
        lastLine = int(line)

    print(numIncrements)
