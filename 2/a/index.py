def jollyJumpers():
    while True:
        try:
            prev = None
            jolly = True
            elements = list(map(int, input().split(' ')))
            elements.pop(0)
            control = [False] * (len(elements) - 1)

            if(len(elements) == 1):
                print("Jolly")
                continue

            for n in elements:
                if(prev == None):
                    prev = n
                else:
                    diff = abs(n - prev)
                    if(diff <= len(control)):
                        control[diff - 1] = True
                        prev = n
            
            for n in control:
                if(n == False):
                    jolly = False
                    break
            
            if(jolly):
                print("Jolly")
            else:
                print("Not jolly")       
        except EOFError:
            return 0


if __name__ == "__main__":
    jollyJumpers()
