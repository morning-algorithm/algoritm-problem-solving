import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
array=[]
p=0
t_sum=0

for i in range(n) :
    p=abs(int((n-1)/2)-i)
    array = list(map(int, input().split()))
    t_sum+=sum(array[p:n-p])
print(t_sum)