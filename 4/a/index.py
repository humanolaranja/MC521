def div7():
    n = int(input())
    elements = []

    for _ in range(n):
        elements.append(int(input()))

    for element in elements:
        if(element % 7 == 0):
            print(element)
        else:
            possible = []
            for i in range(1, 9):
                if((element - i) % 7 == 0 and (element - i) % 10 != 0):
                    if(element - i == 7):
                        possible.append(14)
                    else:
                        possible.append(element - i)
                if((element + i) % 7 == 0 and (element + i) % 10 != 0):
                    possible.append(element + i)

            if(len(possible) == 1 or possible[0] == possible[1]):
                print(possible[0])
            else:
                if(len(str(possible[0])) != len(str(element)) or possible[0] % 10 == 0):
                    print(possible[1])
                
                originalArray = list(map(int, str(element)))
                zeroArray = list(map(int, str(possible[0])))
                oneArray = list(map(int, str(possible[1])))

                zeroPoints = 0
                onePoints = 0


                for j in range(0, len(str(element)) - 1):
                    if(originalArray[j] == zeroArray[j]):
                        zeroPoints += 1
                    if(originalArray[j] == oneArray[j]):
                        onePoints += 1

                if(onePoints >= zeroPoints):
                    print(possible[1])
                else:
                    print(possible[0])


if __name__ == "__main__":
    div7()
