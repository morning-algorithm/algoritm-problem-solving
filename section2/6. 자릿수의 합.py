import sys
#sys.stdin= open("input.txt","rt")

def digit_sum(x):
    cnt=0
    while x/10!=0:
        cnt+=int(x%10)
        x/=10
    return cnt

T=int(input())
a=list(map(int, input().split()))
s=[]

for i in range(T):
    s.append(digit_sum(a[i]))

print(a[s.index(max(s))])

