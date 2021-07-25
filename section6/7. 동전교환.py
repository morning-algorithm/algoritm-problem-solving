import sys
# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline #입력량이 많을 때 입력 속도를 빠르게
# s = input().rstrip(); # 줄바꿈 문자를 제거한 문자열 읽기

def DFS(L,sum):
    global res # 초기화 안했는데 참조하는 경우
    if L>res:
        return
    if sum>m:
        return
    if sum==m:
        if L<res:
            res=L
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])

if __name__=="__main__":
    n= int(input())
    a=list(map(int, input().split()))
    m=int(input())
    res=2147000000
    a.sort(reverse=True) # 큰 값 부터 접근할 수 있도록 내림차순 정렬
    DFS(0,0)
    print(res)
