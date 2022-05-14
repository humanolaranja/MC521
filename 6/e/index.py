def newYearsNumber():
    n = int(input())
    for _ in range (0, n):
        year = int(input())
        div = year / 2020
        mod = year % 2020
        if(div >= mod):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    newYearsNumber()
