def spitProblem():
    n = int(input())
    xPos, dPos = [], []
    for _ in range(n):
        x, d = list(map(int, input().split(' ')))
        xPos.append(x)
        dPos.append(d)

    for i in range(0, len(xPos)):
        for j in range(0, len(dPos)):
            if(xPos[i] + dPos[i] == xPos[j] and xPos[j] + dPos[j] == xPos[i]):
                return "YES"
    return "NO"
                    

if __name__ == "__main__":
    print(spitProblem())
