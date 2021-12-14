from pathlib import Path

# constants
MAP_WIDTH = 1000
INPUT_FILE = 'input.txt'

# compute map index for given coordinate pair
# ---------------------------------------
def computeIndexForXY(x, y):
    return (x % MAP_WIDTH) + (y * MAP_WIDTH)

# mark given line on given map
# ----------------------------------------------------
def markLineSegmentOnMap(startX, startY, endX, endY, map):
    currIndex = -1
    currX = startX
    currY = startY
    
    while not (endX == currX and endY == currY):
        currIndex = computeIndexForXY(currX, currY)
        map[currIndex] += 1
        currX += 1 if endX > currX else -1 if endX < currX else 0
        currY += 1 if endY > currY else -1 if endY < currY else 0

    currIndex = computeIndexForXY(currX, currY)
    map[currIndex] += 1

# find all coordinates on map with more than 1 line segment present
# -----------------------------------------------------------------
def findNumOverlaps(map):
    numOverlaps = 0

    for coord in map:
        if coord > 1:
            numOverlaps += 1

    return numOverlaps

# print map to console for debugging
# ----------------------------------
def printMapDebug(map):
    mapSize = len(map)
    rowIndex = 0
    columnIndex = 0

    while mapSize > rowIndex + (MAP_WIDTH - 1):
        rowString = str(map[rowIndex])
        columnIndex = 1

        while MAP_WIDTH > columnIndex:
            rowString += ' ' + str(map[rowIndex + columnIndex])
            columnIndex += 1
        
        print(rowString)
        rowIndex += MAP_WIDTH

# main
# goal: find the amount of line segment intersections
# ---------------------------------------------------
filePath = Path(__file__).with_name(INPUT_FILE)
with filePath.open('r') as input:
    lines = input.readlines()
    map = [0] * (MAP_WIDTH * MAP_WIDTH)

    for line in lines:
        # parse line segment strings and strip them until we have clean integers going forward
        splitLine = line.split('->')
        
        startPointCoord = splitLine[0].split(',')
        startPointCoord[0] = startPointCoord[0].strip()
        startPointCoord[1] = startPointCoord[1].strip()
 
        endPointCoord = splitLine[1].split(',')
        endPointCoord[0] = endPointCoord[0].strip()
        endPointCoord[1] = endPointCoord[1].strip()

        # uncomment to only consider horizontal or vertical line segments
        if startPointCoord[0] == endPointCoord[0] or startPointCoord[1] == endPointCoord[1]:
            markLineSegmentOnMap(int(startPointCoord[0]), int(startPointCoord[1]), int(endPointCoord[0]), int(endPointCoord[1]), map)

    # printMapDebug(map)

    print('Result: ' + str(findNumOverlaps(map)))
    