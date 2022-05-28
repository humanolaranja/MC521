def vasyaAndCoins():
    t = int(input())
    for _ in range(0, t):
        a, b = list(map(int, input().split(' ')))
        print(b*2+a+1 if a!=0 else 1)

if __name__ == "__main__":
    vasyaAndCoins()
