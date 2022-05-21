wordmap = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}

def loveSong():
    n, q = list(map(int, input().split(' ')))
    s = input()
    index = [0] * (n)

    index[0] = wordmap[s[0]]

    for i in range(1, n):
        index[i] = wordmap[s[i]] + index[i - 1]

    for _ in range (0, q):
        l, r = list(map(int, input().split(' ')))
        print(index[r - 1] - index[(l - 1) - 1] if l > 1 else index[r - 1])


if __name__ == "__main__":
    loveSong()
