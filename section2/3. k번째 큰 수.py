
import sys
#sys.stdin = open("input.txt","rt")

'''me
만들어진 수가 중복되었을 때를 숫자가 중복되었을때로 착각.
3중 for 문 돌릴 생각을 안함.
'''

#answer
N, K = map(int,input().split())
l = list((map(int,input().split())))

s = set() #중복제거를 위해 set에 추가
for i in range(N):
    for j in range(i+1, N):
        for m in range(j+1, N):
            s.add(l[i]+l[j]+l[m]) 

s = sorted(list(s),reverse = True)
print(s[K-1])