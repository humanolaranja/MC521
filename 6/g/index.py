def qaq():
    string = list(input())
    n = len(string)
    count = 0

    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if(string[i] == "Q" and string[j] == "A" and string[k] == "Q"):
                    count += 1
            
    print(count)

if __name__ == "__main__":
    qaq()
