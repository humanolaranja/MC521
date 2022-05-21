def fillingShapes():
    n = int(input())
    output = 0

    if(not(n % 2 == 1)): 
        output = pow(2, n / 2)
    print(int(output))

if __name__ == "__main__":
    fillingShapes()
