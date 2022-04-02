def eventPlanning():
    while True:
        try:
            n, b, h, _ = list(map(int, input().split(' ')))
            price = 1000000

            for _ in range(h):
                p = int(input())
                wBeds = list(map(int, input().split(' ')))
                for beds in wBeds:
                    if(beds >= n):
                        if(n * p < price):
                            price = n * p

            if(price > b):
                print("stay home")
            else:
                print(price)

        except EOFError:
            return 0


if __name__ == "__main__":
    eventPlanning()
