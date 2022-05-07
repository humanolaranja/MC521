def abc():
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        s = input()
        if(n == 1 or s == "10" or s == "01"):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    abc()
