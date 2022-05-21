def lastYearsSubstring():
    n = int(input())

    for _ in range (0, n):
        n = int(input())
        string = list(input())
        if (string[0] == "2" and string[1] == "0" and string[2] == "2" and string[3] == "0" or
            string[0] == "2" and string[1] == "0" and string[2] == "2" and string[n-1] == "0" or
            string[0] == "2" and string[1] == "0" and string[n-2] == "2" and string[n-1] == "0" or
            string[0] == "2" and string[n-3] == "0" and string[n-2] == "2" and string[n-1] == "0" or
            string[n-4] == "2" and string[n-3] == "0" and string[n-2] == "2" and string[n-1] == "0"):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    lastYearsSubstring()
