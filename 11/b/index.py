def queueAtTheSchool():
    n, t = list(map(int, input().split(' ')))

    string = list(map(str, input()))

    for _ in range(0, t):
        i = 1
        while i < n:
            if (string[i] == 'G' and string[i-1] == 'B'):
                string[i] = 'B'
                string[i-1] = 'G'
                i += 1
            i += 1
    
    print(''.join(map(str,string)))


if __name__ == "__main__":
    queueAtTheSchool()
