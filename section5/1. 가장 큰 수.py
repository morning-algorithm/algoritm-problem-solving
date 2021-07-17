import sys
#sys.stdin=open("input.txt", "rt")

n, k= map(int,input().split())
a=list(map(int, str(n)))
stack=[]

"""
while n!=0:
    a.insert(0,n%10)
    n=int(n/10)
"""

for x in a:
    if len(stack)>0:
        while stack and stack[-1]<x and k>0:
            stack.pop()
            k-=1
    stack.append(x)
if k>0:
    stack=stack[:len(stack)-k]

for x in stack:
    print(x, end="")