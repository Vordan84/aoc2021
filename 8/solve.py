from pathlib import Path

# global
MAX_CHARACTERS = 7
INPUT_FILE = 'input.txt'

# return index for given character: a -> 0, b -> 1, ...
def charToIndex(char):
    return ord(char) - ord('a')

# return character for given index: 0 -> a, 1 -> b, ...
def indexToChar(index):
    return chr(index + ord('a'))

# find characters only in second of 2 given strings and return them concatenated
def findUncommonCharacter(str1, str2):
    found = [0] * MAX_CHARACTERS
    
    len1 = len(str1)
    len2 = len(str2)

    for char in range(0, len1):
        found[charToIndex(str1[char])] = 1

    for char in range(0, len2):
        charIndex = charToIndex(str2[char])
        if 1 == found[charIndex]:
            found[charIndex] = -1
        else:
            found[charIndex] = 2
    
    return ''.join([indexToChar(index) for index, char in enumerate(found) if 2 == char])

# main
# part 1: count identifiable digits in output
# part 2: determine actual digits of outputs and sum up
# -------------------------------------------------------------------------------
filePath = Path(__file__).with_name(INPUT_FILE)
with filePath.open('r') as input:
    displays = [display.strip().split('|') for display in input.readlines()]
    
    numKnownDigits = 0
    for display in displays:
        output = display[1].strip().split(' ')
        for value in output:
            length = len(value)
            if 2 == length or 3 == length or 4 == length or 7 == length:
                numKnownDigits += 1

    print('Result - Part1: ' + str(numKnownDigits))

    sum = 0
    for display in displays:
        signal = display[0].strip().split(' ')
        signal.sort(key=len)
        digits = ['x', signal[0], 'x', 'x', signal[2], 'x', 'x', signal[1], signal[len(signal) - 1], 'x']

        # analye signals to populate digit lookup list
        topSegment = findUncommonCharacter(digits[1], digits[7])
        brokenDigit9 = digits[4] + topSegment
        digits[9] = [len6 for len6 in signal if 6 == len(len6) and 1 == len(findUncommonCharacter(brokenDigit9, len6))][0]
        digits[2] = [len5 for len5 in signal if 5 == len(len5) and 1 == len(findUncommonCharacter(digits[9], len5))][0]
        digits[3] = [len5 for len5 in signal if 5 == len(len5) and 1 == len(findUncommonCharacter(digits[2], len5))][0]
        digits[5] = [len5 for len5 in signal if 5 == len(len5) and not digits.__contains__(len5)][0]
        digits[0] = [len6 for len6 in signal if 6 == len(len6) and 2 == len(findUncommonCharacter(digits[5], len6))][0]
        digits[6] = [len6 for len6 in signal if 6 == len(len6) and not digits.__contains__(len6)][0]

        output = display[1].strip().split(' ')
        # for all output digits match them with string in digit lookup list where all characters match and concatenate lookup indices to build output value
        sum += int(''.join([str(index) for signalDigit in output for index, outputDigit in enumerate(digits) if len(signalDigit) == len(outputDigit) and 0 == len(findUncommonCharacter(signalDigit, outputDigit))]))

    print('Result - Part2: ' + str(sum))
