def divisionOfNlogonia():
    n = int(input())
    while n != 0:
        if(n == 0):
            return 0
        maxX, maxY = list(map(int, input().split(' ')))
        for _ in range(n):
            x, y = list(map(int, input().split(' ')))
            if(x == maxX or y == maxY):
                print("divisa")
            if (x < maxX and y > maxY):
                print("NO");
            if (x > maxX and y > maxY):
                print("NE");
            if (x > maxX and y < maxY):
                print("SE");
            if (x < maxX and y < maxY):
                print("SO")
        n = int(input())
        

if __name__ == "__main__":
    divisionOfNlogonia()
