import sys
#sys.stdin=open("input.txt", "rt")

a=[]
c=[0]*9

def print_sdoku(a,c):
    # 행 확인
    for i in range(9):
        c.clear()
        c=[0]*9
        for j in range(9):
            c[a[i][j]-1]=1
        if sum(c)!=9:
            print("NO")
            return
    else:
        # 열 확인
        for i in range(9):
            c.clear()
            c=[0]*9
            for j in range(9):
                c[a[j][i]-1]=1
            if sum(c)!=9:
                print("NO")
                return
        else:
            for i in range(0,7,3):
                for j in range(0,7,3):
                    c.clear()
                    c=[0]*9
                    for k in range(3):
                        for l in range(3):
                            c[a[i+k][j+l]-1]=1
                    if sum(c)!=9:
                        print("NO")
                        return
            else:
                print("YES")
                return

for i in range(9):
    a.append([])
    a[i]=list(map(int, input().split()))
    
print_sdoku(a,c)