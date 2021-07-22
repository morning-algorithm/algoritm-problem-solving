import sys
#sys.stdin = open("input.txt","rt")

#me
'''global..? 리스트는 함수 외부에 선언한 것 그냥 접근이 되는데 일반 변수는 안되네?'''
def dfs(i):
      global isEqual
      
      if isEqual:
            return
      
      if i == n: #마지막 요소 idx + 1 == n
            s1 = 0 #두개의 부분집합
            s2 = 0
            for j in range(len(ch)):
                  if ch[j] == 1:
                        s1 += a[j]
                  else:
                        s2 += a[j]
            if s1 == s2: #두 부분집합의 합이 같으면
                  isEqual = True
                  
      else:
            ch[i] = 0
            dfs(i+1)
            ch[i] = 1
            dfs(i+1)


n = int(input())
ch = [0]*n # x번째 원소가 사용하는 상태인지 체크하는 용도
global isEqual
isEqual = False #두 부분집합의 합이 같은 경우가 있으면 나머지 dfs도 바로 빠져나오기 위한 flag
a = list(map(int,input().split()))
dfs(0) #파라미터에 들어가는 것은 리스트 a의 인덱스
if isEqual:
     print("YES")
else:
      print("NO")

#answer
'''
프로그램을 아예 종료시키는 방법: sys.exit(0)
DFS(idx,sum)해서 sum을 계속 전달하고 마지막 원소까지 다 하면 < 모든 원소의 합 - 누적된 sum >해서 같으면 부분집합의 합이 같은 것으로 판별!

dfs(idx+1, 전달받은 sum+ a[idx]) #사용하는 상태
dfs(idx+1, 전달받은 sum) #사용하지 않는 상태

+ 시간 복잡도를 줄이는 방법:
      재귀함수 호출 도중 누적 sum이 total/2를 넘어버리면 절대 부분집합의 합이 같을 수 없다.
      더이상 dfs할 필요 없다. 바로 커트해버린다.
      바로 return 한다.

      여기서 누군가 생각한다. sum == total//2로 바로 부분집합 합이 같은것이라고 판별하면 안되나?
      => 안됨! 홀수인경우 //2로 인해서 소숫점이 깎여 같지 않은데 같다고 나와버릴수도 있다. 
'''
