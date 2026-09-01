def solution(problemInput: list):
    x, y = problemInput[0]

    for i in range(1, len(problemInput)):
        k, m = problemInput[i]
        print(min(k, x) * min(m, y))

def formatTestCase():
    bermudaRectangle = input()
    x, y = bermudaRectangle.split()
    x = int(x)
    y = int(y)

    res = [(x, y)]

    for _ in range(y):
        testArea = input()
        k, m = testArea.split()
        k = int(k)
        m = int(m)

        res.append((k, m))

    return res

def main():
    numOfTestCases = int(input())
    for _ in range(numOfTestCases):
        solInput = formatTestCase()
        solution(solInput)

if __name__ == '__main__':
    main()