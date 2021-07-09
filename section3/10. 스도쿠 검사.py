def check(num):
    #모든 행, 열 검사
    for i in range(9):
        row_num = [0]*10
        col_num = [0]*10
        for j in range(9):
            row_num[num[i][j]] = 1
            col_num[num[j][i]] = 1

        if sum(row_num) != 9 or sum(col_num) != 9:
           return False

    for i in range(3):
        for j in range(3):
            box_num = [0]*10
            for k in range(3):
                for s in range(3):
                    box_num[num[i*3+k][j*3+s]] = 1

            if sum(box_num) != 9:
                return False
    return True        

num = [list(map(int, input().split())) for _ in range(9)]

if check(num):
    print("YES")
else:
    print("NO")
