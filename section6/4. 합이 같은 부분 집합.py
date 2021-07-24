import sys
#sys.stdin=open("input.txt", "r")

def DFS(i):
    global sum1, sum2, flag
    if i == n:
        for j in range(n):
            if res[j][1]==1:
                sum1+=res[j][0]
            else :
                sum2+=res[j][0]
        if sum1==sum2:
            flag=1
        else:
            sum1=0
            sum2=0
    else:
        res[i][1]=1 # O - 부분 집합 포함
        DFS(i+1)
        res[i][1]=0 # X - 부분 집합 제외
        DFS(i+1)


if __name__=="__main__":
    n= int(input())
    a=list(map(int, input().split()))
    res=[]
    for i in range(n):
        res.append([])
        res[i].append(a[i])
        res[i].append(0)
    flag=0
    sum1=0
    sum2=0
    DFS(0)
    if flag==0:
        print("NO")
    else:
        print("YES")

# res=[(1,0), (3,0),(5,0),(7,0),(9,0)] -> tuple자료구조는 immutable
# print(res[1]) -> (3,0)
# print(res[1][0])