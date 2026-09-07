#2254D

def solution(arrayB):
    numberedArray = []

    for cnt, i in enumerate(arrayB):
        numberedArray.append([i, cnt])

    numberedArray.sort()

    i = 0
    currSum = 0
    currentSameNumber = numberedArray[0]
    prevShadowAmt = 0

    for j in range(1, len(arrayB)):
        if numberedArray[j][0] != currentSameNumber:
            currentSameNumber = numberedArray[j][0]
            shadowNumCnt = j - i
            if currentSameNumber % shadowNumCnt :
                return [-1]
            
            prevShadowAmt = (currentSameNumber - currSum) // shadowNumCnt
            currSum += prevShadowAmt * shadowNumCnt

            while i < j:
                numberedArray[i][0] = prevShadowAmt
                i += 1

    while i < len(arrayB):
        numberedArray[i][0] = prevShadowAmt + 1
        i += 1

    arrayA = arrayB
    for i, index in numberedArray:
        arrayA[index] = i

    return arrayA

def getInput():
    
    n = int(input())
    inputArray = list(map(int, input().split()))
    return n, inputArray

def main():
    testCases = int(input())

    for _ in range(testCases):
        _, arrayB = getInput()

        ans = solution(arrayB)

        print(*ans)

if __name__ == "__main__":
    main()