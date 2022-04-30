# https://code.activestate.com/recipes/252178/
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

def ACMICPC():
    elements = list(map(int, input().split(' ')))
    allElements = list(all_perms(elements))
    for element in allElements:
        if(element[0] + element[1] + element[2] == element[3] + element[4] + element[5]):
            return "YES"
    return "NO"


if __name__ == "__main__":
    print(ACMICPC())
