from pathlib import Path

INPUT_FILE = 'input.txt'

# returns 0, if bit at given offset is not set
def isBitSet(toTest, offset):
    mask = 1 << offset
    return (toTest & mask)

# returns integer for either oxygen or co2 rating
def findRating(findOxygen, lines, bitCounter, offset):
    nextBitCounter = 0
    remainingLines = []
    searchingFor1 = (float(bitCounter) >= float(len(lines) * 0.5)) if findOxygen else (float(bitCounter) < float(len(lines) * 0.5))
    
    for line in lines:
        if searchingFor1:
            if isBitSet(int('0b' + line.rstrip(), 0), offset) != 0:
                remainingLines.append(line)

                if 1 <= offset and isBitSet(int('0b' + line.rstrip(), 0), offset - 1) != 0:
                    nextBitCounter += 1
        else:
            if isBitSet(int('0b' + line.rstrip(), 0), offset) == 0:
                remainingLines.append(line)

                if 1 <= offset and isBitSet(int('0b' + line.rstrip(), 0), offset - 1) != 0:
                    nextBitCounter += 1

    nextOffset = offset - 1
    if (1 == len(remainingLines)):
        return int('0b' + remainingLines[0].rstrip(), 0)
    else:
        return findRating(findOxygen, remainingLines, nextBitCounter, nextOffset)

# main entry
filePath = Path(__file__).with_name(INPUT_FILE)
with filePath.open('r') as input:
    lines = input.readlines()
    inputBitLength = len(lines[0]) - 1

    # determine number of set bits in first row
    bitCounter = 0

    for line in lines:
        if isBitSet(int('0b' + line.rstrip(), 0), inputBitLength - 1) != 0:
            bitCounter += 1

    # filter life support rating
    oxygen = findRating(True, lines, bitCounter, inputBitLength - 1)
    co2 = findRating(False, lines, bitCounter, inputBitLength - 1)

    print('Result: ' + str(oxygen * co2))
