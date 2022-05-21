def theCakeIsALie():
    t = int(input())

    for _ in range(0, t):
        n, m, k = list(map(int, input().split(' ')))
        print("YES" if n * m - 1 == k else "NO")


if __name__ == "__main__":
    theCakeIsALie()
