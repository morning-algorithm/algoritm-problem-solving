
import sys
from collections import Counter

#sys.stdin = open("input.txt","rt")

N,M = map(int,input().split())

suml = list()

for n in range(1,N+1):
    for m in range(1,M+1):
        suml.append(n+m)

dic = Counter(suml)
max = max(dic.values())
result = list(filter(lambda x:x[1] == max, dic.items()))
result.sort()


for r in result:
    print(r[0],end='')
