import sys
#sys.stdin = open("input.txt","rt")

#me
'''
부분집합의 형태
왼쪽가지: 상담o
오른쪽 가지: 상담x
                                     1일
 1일+상담에 걸리는시간    1일+1(다음날)

 N+1이 되는 날 휴가를감. N+1을 넘어가면 안됨.
 '''

def dfs(i,sum):
      global max

      if i >  n+1 : # 휴가날 초과
            return
      elif i == n+1 :
            if sum > max:
                  max= sum
            return

      dfs(i+a[i][0],sum + a[i][1]) #사용
      dfs(i+1,sum) #사용x
            
      
n = int(input())
a = [0]*(n+1)
max = -1

for i in range(1,n+1):
      a[i] = tuple(map(int,input().split()))#인덱스 번호를 날짜로 사용하겠다.

dfs(1,0) 
print(max)
