def meximization():
    n = int(input())
    for _ in range(n):
        input()
        items = list(map(int, input().split(' ')))
        items.sort()
        previous = items[0]
        unique = [previous]
        repeated = []

        for i in range (len(items)):
            if(i == 0):
                continue
            element = items[i]
            if(element == previous):
                repeated.append(element)
            else:
                unique.append(element)
            previous = element

        output = unique + repeated  
        print(' '.join(map(str, output)))

if __name__ == "__main__":
    meximization()
