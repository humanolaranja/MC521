def soldierandBananas():
    k, n, w = list(map(int, input().split(' ')))
    output = 0
    
    for i in range(1, w+1):
        output += i*k

    if(output <= n):
        output = n
    
    print(output-n)


if __name__ == "__main__":
    soldierandBananas()
