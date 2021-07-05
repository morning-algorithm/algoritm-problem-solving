import sys
#sys.stdin= open("input.txt","rt")

n=int(input())
s=list(map(int, input().split()))
a=int(round(sum(s)/len(s),0))

min = float('inf')
min_i = -1
for i in range(n):
    if abs(s[i]-a)<min :
        min = abs(s[i]-a)
        min_i = i
    elif abs(s[i]-a)==min:
        if s[i]>s[min_i]:#기존 값이 더 작은 경우(음수인 경우)
            min_i = i
        elif s[i]==s[min_i] and i<min_i:#기존 값과 같은 값인 경우 기존 값의 인덱스보다 작으면 
            min_i=i
        else: 
            continue
print(a, min_i+1)