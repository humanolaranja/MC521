def maximumCakeTastiness():
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        a = list(map(int, input().split(' ')))
        a.sort()
        print(a[n-1] + a[n-2])

if __name__ == "__main__":
    maximumCakeTastiness()
