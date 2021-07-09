
import sys
#sys.stdin = open("input.txt","rt")

#me
'''
45를 숫자를 중복해서도 만들 수 있기때문에 단순히 합으로만 검사하면 틀림

a = [list(map(int,input().split())) for _ in range(9)]

def check_row_and_column():
    for i in range(9):
        sum_r = 0
        sum_c = 0
        
        for j in range(9):
            sum_r += a[i][j]
            sum_c += a[j][i]
        print(sum_r,sum_c)
        if sum_r != 45 or sum_c != 45:
            return False
    return True
 
def check_box():
    for i in range(0,9,3):
        for j in range(0,9,3):
            sum_b = 0
            for k in range(3):
                sum_b += sum(a[i+k][j:j+3])
            if sum_b != 45:
                return False
    return True

if check_row_and_column() and check_box():
    print("YES")
else:
    print("NO")
'''

#answer
'''
풀이: check 배열을 만들어서 숫자가 나오면 1로 만들고 
배열을 다 합했을 때 9가 안나오면 중복임
'''

a = [list(map(int,input().split())) for _ in range(9)]

def check_row_and_column():
    for i in range(9):
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[i][j]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    return True

def check_box():
    for i in range(0,9,3):
        for j in range(0,9,3):
            ch3 = [0]*10
            for k in range(i,i+3):
                for s in range(j,j+3):
                    ch3[a[k][s]] = 1
                
            if sum(ch3) != 9:
                return False
    return True

if check_row_and_column() and check_box():
    print("YES")
else:
    print("NO")