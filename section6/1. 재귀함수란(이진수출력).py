import sys
#sys.stdin=open("input.txt", "r")


def divNum(x):
    if x == 0 or x == 1:
        return str(x)
    else:
        return str(x%2) + divNum(x//2)
        

n = int(input())
print(divNum(n)[::-1])


'''
def divNum(x):
    if x == 0 or x == 1:
        print(x, end="")
    else:
        divNum(x//2)
        print(x%2, end="")
        

n = int(input())
divNum(n)
'''

    
