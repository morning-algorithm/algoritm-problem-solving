import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
nList = list(map(int, input().split()))

m = int(input())
mList = list(map(int, input().split()))

c = list()
c += nList
c += mList
c.sort()

print(c)
