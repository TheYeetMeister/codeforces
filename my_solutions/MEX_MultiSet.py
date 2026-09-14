#2259D

def solution(n, arrayA):
    labels = {0: "A", 1: "B", 2: "C"}

    res = [-1 for _ in range(n)]
    labeled = [-1 for _ in range(n)]

    for cnt, i in enumerate(arrayA):
        labeled[cnt] = (i, cnt)

    labeled.sort()

    mexes = [0, 0, 0]

    currNum = 0
    cnt = 0
    for num, index in labeled:
        if num != currNum:
            currNum = num
            cnt = 0

        res[index] = labels[cnt % 3]
        if mexes[cnt % 3] == currNum:
            mexes[cnt % 3] += 1
        cnt += 1

    if sum(mexes) < 2 * max(mexes):
        return []
    return res


def getInput():
    n = int(input())
    inputArray = list(map(int, input().split()))

    return n, inputArray

def main():
    testCnt = int(input())

    for _ in range(testCnt):
        n, arrayA = getInput()

        res = solution(n, arrayA)

        if res:
            print("YES")

            for x in res:
                print(x, end="")
            print()
        else:
            print("NO")

if __name__ == "__main__":
    main()