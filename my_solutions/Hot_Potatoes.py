#2255A

def solution(n: int, k: int, state: str):
    count = 2 * n
    nextPotatoHolders = set()
    potatoHolders = set()
    prevPotatoHolders = set()

    for i, hasPotato in enumerate(state):
        if hasPotato == "1":
            potatoHolders.add(i)

    for _ in range(k):
        for i in potatoHolders:
            left = i - 1 if i > 0 else count - 1
            right = i + 1 if i < count - 1 else 0

            if left not in prevPotatoHolders and left not in nextPotatoHolders:
                nextPotatoHolders.add(left)
            elif right not in prevPotatoHolders and right not in nextPotatoHolders:
                nextPotatoHolders.add(right)
            else:
                nextPotatoHolders.add(i)

            prevPotatoHolders = potatoHolders
            potatoHolders = nextPotatoHolders
            nextPotatoHolders = set()

    redTeamPoints = n
    blueTeamPoints = n

    for i in potatoHolders:
        if i % 2 == 1:
            redTeamPoints -= 1
        else:
            blueTeamPoints -= 1

    return redTeamPoints, blueTeamPoints




def getCaseInput():
    n, k = map(int, input().split())
    potatoState = input()

    return int(n), int(k), potatoState

def main():
    testCaseCnt = int(input())

    for _ in range(testCaseCnt):
        n, k, state = getCaseInput()

        redTeamPoints, blueTeamPoints = solution(n, k, state)
        print(redTeamPoints, blueTeamPoints)


if __name__ == "__main__":
    main()