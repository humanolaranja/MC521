def loveTriangle():
    n = int(input())
    f = list(map(int, input().split(' ')))

    for j in range(1, n):
        if(f[f[f[j-1]-1]-1] == j):
            return "YES"

    return "NO"

if __name__ == "__main__":
    print(loveTriangle())
