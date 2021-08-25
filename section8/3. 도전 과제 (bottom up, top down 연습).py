import sys
sys.stdin = open("input.txt", "r")
# 도전 과제 1 : 계단 오르기 (Top-down)
# 도전 과제 2 : 돌다리 건너기(Bottom-up)

# 도전 과제 1
def DFS(v):
    if dy1[v]>0:
        return dy1[v]
    if v==1 or v==2:
        return v
    else:
        dy1[v]=DFS(v-1)+DFS(v-2)
        return dy1[v]

if __name__=="__main__":
    n=int(input())
    dy1=[0]*(n+1)
    print(DFS(n))
# 도전 과제 2
m= int(input())
dy2=[0]*(m+1)

dy2[1]=1
dy2[2]=2

for i in range(3, m+1):
    dy2[i]=dy2[i-1]+dy2[i-2]
    
print(dy2[m])

