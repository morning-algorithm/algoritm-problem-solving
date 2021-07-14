n = int(input())
num = list(map(int, input().split()))
num.insert(0, 0) #1을 1번부터 시작하기 위
origin = [0]*n
for i in range(1, n+1):
    print(i)
    for j in range(n):
        #origin[j]가 0이 아니라면 그냥 무시하고 j+1을 
        if num[i] == 0 and origin[j] == 0: #자기 자리를 찾아감
            print('origin2: ', j, ' ', origin[j])
            origin[j] = i
            break
        elif origin[j] == 0:
            print('origin1: ', j, ' ', num[i])
            num[i] -= 1 #빈자리를 찾아가고 있음

for x in origin:
    print(x, end=' ')
