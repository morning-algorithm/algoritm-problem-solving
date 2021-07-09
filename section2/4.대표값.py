
import sys
#sys.stdin = open("input.txt","rt")

N = int(input())
l = list(map(int,input().split()))

average = round(sum(l) / N )

min = average - l[0]
min_idx = 0
for i in range (1,len(l)):
    diff = l[i] - average
    if abs(diff) < abs(min) :
        min = diff
        min_idx = i
    elif abs(diff) == abs(min) and diff > min :
        min = diff
        min_idx = i
print(average, min_idx+1)