def kefaAndFirstSteps():
    n = int(input())
    line = list(map(int, input().split(' ')))
    count, countLocal = 1, 1

    for i in range (1, n):
        if(line[i] >= line[i-1]):
            countLocal += 1
        else:
            countLocal = 1

        if(countLocal > count):
            count = countLocal
            
    print(count)

if __name__ == "__main__":
    kefaAndFirstSteps()
