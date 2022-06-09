def badge():
    n = int(input())
    p = list(map(int, input().split(' ')))
    output = []

    for i in range(0, n):
        array, temp = [0] * (n), i
        while (array[temp] < 2):
            array[temp] += 1
            temp = p[temp] - 1
        output.append(temp + 1)
    
    print(' '.join(map(str,output)))

if __name__ == "__main__":
    badge()
