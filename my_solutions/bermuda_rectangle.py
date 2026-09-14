#2257D
from collections import namedtuple
import math

bermudaRect = namedtuple("bermudaRect", ["height",  "width", "prefixSum"])

def getBermudaRectangles(area):
    potentialRects = []
    prefixSum = 0

    for i in range(1, int(math.sqrt(area)) + 1):
        if area % i == 0:
            width = i
            height = area // i

            potentialRects.append((width, height))
            potentialRects.append((height, width))

    potentialRects.sort()
    prefixSum = 0
    lastWidth = 0
    res = []

    for width, height in potentialRects:
        prefixSum += (width - lastWidth) * height
        lastWidth = width
        res.append(bermudaRect(height, width, prefixSum))

    return res

def calAreaInBermudaRectangle(bermudaRects, n, width, height):
    left, right = 0, n - 1
    potentialCutOff = n

    # Find cutOff
    while left <= right:
        mid = left + (right - left) // 2

        if bermudaRects[mid].height > height:
            left = mid + 1
        else:
            potentialCutOff = mid
            right = mid - 1

    if potentialCutOff == 0:
        wBound, leftPrefix = 0, 0
    else:
        wBound = bermudaRects[potentialCutOff - 1]. width
        leftPrefix = bermudaRects[potentialCutOff - 1].prefixSum

    if width <= wBound:
        return width * height

    #findEnd
    left, right = 0, n - 1
    potentialLimit = n - 1

    while left <= right:
        mid = left + (right - left) // 2

        if bermudaRects[mid].width < width:
            left = mid + 1
        else:
            potentialLimit = mid
            right = mid - 1

    rightPrefix = bermudaRects[potentialLimit].prefixSum

    if bermudaRects[potentialLimit].width > width:
        rightPrefix -= (bermudaRects[potentialLimit].width - width) * bermudaRects[potentialLimit].height
        
    return height * wBound + rightPrefix - leftPrefix

    

def solution(area, queryCnt, queries):
    res = []

    bermudaRects = getBermudaRectangles(area)
    n = len(bermudaRects)

    for width, height in queries:
        res.append(calAreaInBermudaRectangle(bermudaRects, n, width, height))

    return res

def getInput():
    area, queryCnt = map(int, input().split())
    queries = []

    for _ in range(queryCnt):
        queries.append(list(map(int, input().split())))

    return area, queryCnt, queries

def main():
    testCnt = int(input())

    for _ in range(testCnt):
        area, queryCnt, queries = getInput()

        res = solution(area, queryCnt, queries)

        for i in res:
            print(i)

if __name__ == "__main__":
    main()