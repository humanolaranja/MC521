def codecraft():
    m = input()
    n = int(input())
    array = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    array = array + array + array + array + array + array + array + array + array + array

    index = array.index(m)
    print(array[index + n])


if __name__ == "__main__":
    codecraft()
