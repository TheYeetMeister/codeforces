#2254E
from collections import deque
import bisect

def solution(arrayB):
    sumOfB = sum(arrayB)

    if not sumOfB > 0:
        return [-1]

    arrayB.sort()
    positiveArray = deque()
    nonPosArray = []

    for i in arrayB:
        if i > 0:
            positiveArray.append(i)
        else:
            bisect.insort(nonPosArray, i)

    res = [positiveArray.popleft()]
    while positiveArray or nonPosArray:
        if nonPosArray and res[-1] + nonPosArray[-1] > 0:
            idx = bisect.bisect_left(nonPosArray, -res[-1])
            value = nonPosArray.pop(idx - 1)
        else:
            value = positiveArray.popleft()

        res.append(res[-1] + value)

    return res

def getInput():
    sizeOfArray = int(input())
    arrayB = list(map(int, input().split()))

    return sizeOfArray, arrayB

def main():
    testCaseCnt = int(input())

    for _ in range(testCaseCnt):
        _, arrayB = getInput()

        ans = solution(arrayB)

        print(*ans)


if __name__ == '__main__':
    main()