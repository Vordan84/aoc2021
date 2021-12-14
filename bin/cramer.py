# import numpy as np

# use Cramer's rule to solve equations with 2 unknowns and returns whether result for s and t proofs an intersection
# ------------------------------------------------------------------------------------------------------------------ 

def haveIntersection(lineSegment1, lineSegment2):
    # variables for determining x coordinate of intersection
    sxFactor = lineSegment1[2] - lineSegment1[0]
    txFactor = lineSegment2[2] - lineSegment2[0]
    xResult = lineSegment2[0] - lineSegment1[0]
    # variables for determining y coordinate of intersection
    syFactor = lineSegment1[3] - lineSegment1[1]
    tyFactor = lineSegment2[3] - lineSegment2[1]
    yResult = lineSegment2[1] - lineSegment1[1]

    '''
    # filter parallel segments
    v1 = np.array([sxFactor, syFactor])
    v2 = np.array([txFactor, tyFactor])
    if 0 == np.cross(v1, v2):
        return False
    '''

    # Cramer's rule - check for parallel segments BEFORE to avoid division by 0
    stDivisor = (sxFactor * tyFactor) - (txFactor * syFactor)
    if 0 != stDivisor:
        s = (xResult * tyFactor) - (txFactor * yResult) / stDivisor
        t = (sxFactor * yResult) - (xResult * syFactor) / stDivisor

        # FIXME: actually compute intersection coordinates with s and t

        # segments intersect if both s and t absolutes are between 0 and 1, otherwise lines intersect outside given segments
        return 1.0 >= np.abs(s) and 0.0 <= np.abs(s) and 1.0 >= np.abs(t) and 0.0 <= np.abs(t)
    return False


# brute-force compare all line segments with all other line segments; count and return the number of intersections
# ----------------------------------------------------------------------------------------------------------------
def findLineSegmentIntersections(lineSegments):
    numIntersectingLineSegments = 0

    for segment in lineSegments:
        if segment[0] == segment[2] or segment[1] == segment[3]:
            for comparedSegment in lineSegments:
                same = segment[0] == comparedSegment[0] and segment[1] == comparedSegment[1] and segment[2] == comparedSegment[2] and segment[3] == comparedSegment[3]

                if False == same and (comparedSegment[0] == comparedSegment[2] or comparedSegment[1] == comparedSegment[3]):
                    if haveIntersection(segment, comparedSegment):
                        numIntersectingLineSegments += 1

    return numIntersectingLineSegments
