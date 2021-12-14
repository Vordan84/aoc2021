from pathlib import Path

INPUT_FILE = 'input.txt'

# ---------------------------
def isBitSet(toTest, offset):
    mask = 1 << offset
    return (toTest & mask)

# ---------------------------------------------
filePath = Path(__file__).with_name(INPUT_FILE)
with filePath.open('r') as input:
    lines = input.readlines()
    commonBitThreshold = int(len(lines) / 2)
    inputBitLength = len(lines[0]) - 1
    print('Threshold: ' + str(commonBitThreshold))
    print('BitLength: ' + str(inputBitLength))

    # determine number of set bits per row
    bitCounter = [0] * inputBitLength
    
    for line in lines:
        bit = 0
        while bit < inputBitLength:
            if isBitSet(int('0b' + line.rstrip(), 0), bit) != 0:
                bitCounter[bit] += 1
            bit += 1
    print('BitCount:' + str(bitCounter))

    # build binary representations for gamma and epsilon based on counted bits
    gamma = ""
    epsilon = ""
    bit = inputBitLength - 1

    while bit >= 0:
        if bitCounter[bit] > commonBitThreshold:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
        bit -= 1

    print(gamma)
    print(epsilon)

    print('Result: ' + str(int('0b' + gamma, 0) * int('0b' + epsilon, 0)))
