import sys
#sys.stdin=open("input.txt", "r")

def DFS(i):
    if i == n:
        for j in range(n):
            if res[j]==1:
                print(j+1, end=" ")
        print()
    else:
        res[i]=1 # O - 부분 집합 포함
        DFS(i+1)
        res[i]=0 # X - 부분 집합 제외
        DFS(i+1)

if __name__=="__main__":
    n= int(input())
    res=[0]*n # 부분 집합의 숫자 0, 1로 여부 표시
    DFS(0)
