from pathlib import Path

# constants
NUMBERS_PER_ROW = 5
INPUT_FILE = 'input.txt'

# load and cleanup draws
#-----------------------
def loadDraws(draws):
    cleanedDraws = []    
    dirtyDraws = draws.split(',')

    for draw in dirtyDraws:
        cleanedDraws.append(int(draw.rstrip()))

    return cleanedDraws

# load and cleanup bingo boards
#------------------------------
def loadBingoBoards(boardInput):
    boardRowData = []
    
    for row in boardInput:
        rowData = row.split(' ')

        if len(rowData) >= NUMBERS_PER_ROW:
            for data in rowData:
                dataSize = len(data)

                if 0 != dataSize:
                    # clean all line break crap for valid data and write clean integer values to boardRowData
                    boardRowData.append(int(data.rstrip()))

    return boardRowData, int(len(boardRowData) / (NUMBERS_PER_ROW * NUMBERS_PER_ROW))

# returns either -1 or the board index where a row or column with NUMBERS_PER_ROW markings was found
#---------------------------------------------------------------------------------------------------
def canHasBingo(boardNumbers, boardMarkIndex, draws, drawIndex):
    isBingo = False

    # determine boardIndex
    boardIndex = int(boardMarkIndex / (NUMBERS_PER_ROW * NUMBERS_PER_ROW))

    # determine whether whole row around boardMarkIndex is marked
    rowFirstIndex = boardMarkIndex - (boardMarkIndex % NUMBERS_PER_ROW)
    rowLastIndex = rowFirstIndex + (NUMBERS_PER_ROW - 1)
    rowSearchIndex = rowFirstIndex
    rowMarkedCounter = 0

    while rowLastIndex >= rowSearchIndex:
        # skip freshly marked number... we know it's marked... duh
        if rowSearchIndex != boardMarkIndex:
            drawNumber = boardNumbers[rowSearchIndex] 

            try:
                draws.index(drawNumber, 0, drawIndex)
                rowMarkedCounter += 1
            except ValueError:
                break

        rowSearchIndex += 1
        # BINGO - all numbers in row had been drawn already
        if rowMarkedCounter == NUMBERS_PER_ROW - 1:
            isBingo = True
            return boardIndex

    # determine whether whole column around boardMarkIndex is marked
    if not isBingo:
        colFirstIndex = (NUMBERS_PER_ROW * NUMBERS_PER_ROW * boardIndex) + (boardMarkIndex % NUMBERS_PER_ROW)
        colLastIndex = colFirstIndex + (NUMBERS_PER_ROW * (NUMBERS_PER_ROW - 1))
        colSearchIndex = colFirstIndex
        colMarkedCounter = 0

        while colLastIndex >= colSearchIndex:
            # skip freshly marked number... we know it's marked... duh
            if colSearchIndex != boardMarkIndex:
                drawNumber = boardNumbers[colSearchIndex] 

                try:
                    draws.index(drawNumber, 0, drawIndex)
                    colMarkedCounter += 1
                except ValueError:
                    break

            colSearchIndex += NUMBERS_PER_ROW
            # BINGO - all numbers in row had been drawn already
            if colMarkedCounter == NUMBERS_PER_ROW - 1:
                return boardIndex     

    return -1

# returns the sum of all unmarked numbers in board multiplied with the last drawn number
#---------------------------------------------------------------------------------------
def computeBoardScore(boardNumbers, boardIndex, draws, drawIndex):
    
    # determine scope of board within list
    boardFirstIndex = NUMBERS_PER_ROW * NUMBERS_PER_ROW * boardIndex
    boardLastIndex = boardFirstIndex + ((NUMBERS_PER_ROW * NUMBERS_PER_ROW) - 1)
    boardSearchIndex = boardFirstIndex
    boardUnmarkedSum = 0

    # sum up all still unmarked numbers
    while boardLastIndex >= boardSearchIndex:
        drawNumber = boardNumbers[boardSearchIndex]
        boardSearchIndex += 1

        try:
            draws.index(drawNumber, 0, drawIndex + 1) # add to draw index so winning number considered marked
        except ValueError: # not found, sum up
            boardUnmarkedSum += drawNumber

    return boardUnmarkedSum * draws[drawIndex]

# main
# goal: find first board to win and return its goal
#----------------------------------------------
filePath = Path(__file__).with_name(INPUT_FILE)
with filePath.open('r') as input:
    lines = input.readlines()

    # load bingo data
    draws = loadDraws(lines[0])
    boardNumbers, numBoards = loadBingoBoards(lines)
    bingoBoardIndex = -1
    bingoDrawIndex = -1

    # play bingo: mark number, check for bingo
    for drawIndex, draw in enumerate(draws):
        if NUMBERS_PER_ROW - 1 <= drawIndex:
            searchDone = False
            searchIndex = 0
            boardMarkIndex = -1
            print('Testing for Bingo with ' + str(draw))
            
            while not searchDone:
                try:
                    boardMarkIndex = boardNumbers.index(int(draw), searchIndex)
                    bingoBoardIndex = canHasBingo(boardNumbers, boardMarkIndex, draws, drawIndex)
                    bingoDrawIndex = drawIndex

                    if -1 != bingoBoardIndex:
                        searchDone = True

                    searchIndex = boardMarkIndex + 1
                    if len(boardNumbers) <= searchIndex:
                        searchDone = True 
                except ValueError:
                    searchDone = True

            if -1 != bingoBoardIndex:
                print('DONE')
                break

    score = computeBoardScore(boardNumbers, bingoBoardIndex, draws, bingoDrawIndex)
    print(score)
