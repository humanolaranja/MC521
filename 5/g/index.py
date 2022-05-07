def checkIsValidBall(a, b):
    if(a == b or a > b + 2 or a < b - 2):
        return False
    return True

def bearandThreeBalls():
    n = int(input())
    array = list(map(int, input().split(' ')))
    array.sort()

    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if(checkIsValidBall(array[i], array[j]) and checkIsValidBall(array[i], array[k]) and checkIsValidBall(array[j], array[k])):
                    return "YES"
    return "NO"


if __name__ == "__main__":
    print(bearandThreeBalls())
