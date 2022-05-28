def maximumCakeTastiness():
    t = int(input())
    for _ in range(0, t):
        n, b, x, y = list(map(int, input().split(' ')))
        total, aux = 0, 0
        for _ in range (0, n):
            aux = aux - y if aux + x > b else aux + x
            total += aux

        print(total)

if __name__ == "__main__":
    maximumCakeTastiness()
