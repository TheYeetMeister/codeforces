#2254C2

def verifyInput(arrayA, arrayB, start, step):
    zeroCnt = 0
    oneCnt = 0

    for i in range(start, len(arrayA), step):
        if arrayA[i] == 0:
            zeroCnt += 1
        else:
            oneCnt += 1

        if arrayB[i] == 0:
            zeroCnt -= 1
        else:
            oneCnt -= 1

    return zeroCnt == 0 and oneCnt == 0


def solution(arrayA, arrayB):
    if not verifyInput(arrayA, arrayB, 0, 2) or not verifyInput(arrayA, arrayB, 1, 2):
        return -1

    res = 0
    for i in range(0, len(arrayA), 2):
        if arrayA[i] != arrayB[i]:
            for j in range(i + 2, len(arrayB), 2):
                prev = arrayB[j]
                arrayB[j] = arrayB[j - 2]

    return 0


def getInput():
    n = int(input())
    arrayA = list(map(int, input().split()))
    arrayB = list(map(int, input().split()))

    return arrayA, arrayB

def main():
    testCnt = int(input())

    for _ in range(testCnt):
        arrayA, arrayB = getInput()

        res = solution(arrayA, arrayB)

        print(res)

if __name__ == '__main__':
    main()