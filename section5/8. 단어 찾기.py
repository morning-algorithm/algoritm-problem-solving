import sys
#sys.stdin=open("input.txt", "rt")

n= int(input())
str=[]
for i in range(n):
    str.append(input())

for i in range(n-1):
    str.remove(input())

print(str[0])