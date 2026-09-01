#2257C

import sys
sys.setrecursionlimit(1 << 20)

def solution(vertexCnt, parents, beaverDamCnt, beaverDams):
    damsSet = set(beaverDams)
    adj = {v: [] for v in range(vertexCnt)}

    for i in range(len(parents)):
        adj[parents[i] - 1].append(i + 1)


    camerasNeeded = beaverDamCnt - 1
    res = [camerasNeeded]

    def dfs(v):
        hasDam = v + 1 in damsSet

        for i in adj[v]:
            childHasDam = dfs(i)

            if hasDam and childHasDam:
                res.append(i + 1)

            hasDam = hasDam or childHasDam

        return hasDam

    dfs(0)

    print(*res)

def formatInput():
    vertexCnt = int(input())
    parents = list(map(int, input().split()))
    beaverDamCnt = int(input())
    beaverDams = list(map(int, input().split()))

    return vertexCnt, parents, beaverDamCnt, beaverDams

    

def main():
    testcaseCnt = int(input())

    for _ in range(testcaseCnt):
        vertexCnt, parents, beaverDamCnt, beaverDams = formatInput()
        solution(vertexCnt, parents, beaverDamCnt, beaverDams)

if __name__ == "__main__":
    main()