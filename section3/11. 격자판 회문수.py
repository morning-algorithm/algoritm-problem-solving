import sys
#sys.stdin = open("input.txt","rt")

#me
a = [list(map(int,input().split())) for _ in range(7)]
b = list(map(list, zip(*a)))

cnt = 0
for i in range (7):
    for j in range(3):
        al = a[i][0+j : 4+j+1]
        bl = b[i][0+j : 4+j+1]

        if al  == list(reversed(al)):
            cnt += 1
        if bl  == list(reversed(bl)):
            cnt += 1

print(cnt)

#answer
'''
옆 방향: slice, [::-1]를 이용해서 역순을 확인
아래 방향:
    2차원에서 아래방향으로는 slice 불가. 
    2중포문에서 for문을 하나 더 추가.
    for k in range(2):
        if board[j+k][i] != board[j+5-k-1][i]:
            break
'''