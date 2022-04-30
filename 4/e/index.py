def phoneNumbers():
    size = int(input())
    numbers = list(map(int, input()))

    maxPhones = size / 11
    maxPossiblePhones = numbers.count(8)

    if(maxPossiblePhones >= maxPhones):
        print(int(maxPhones))
    else:
        print(int(maxPossiblePhones))  

if __name__ == "__main__":
    phoneNumbers()
