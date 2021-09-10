import sys
sys.stdin = open("input.txt","r")

#me
'''
일부는 맞고 일부는 틀림.왜그럴까했더니.. 이건 수열문제가아니였다. 벽돌을 순서를 마음껏 바꿔도된다..

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.insert(0,0)
dy = [0] * (n+1) # 각 항을 마지막으로 했을때 최대로 쌓을 수 있는 높이
dy[1] = arr[1][1]
res = dy[1] #첫번째 항까지만 있을때의 답


for i in range(2, n+1):
    max = 0
    for j in range(i-1,0,-1):
        if arr[i][0] < arr[j][0] and arr[i][2] < arr[j][2] and max < dy[j] : # 밑에 있는게 넓이가 넓어야하고 무게가 커야한다. 만족한다면 쌓아온 높이가 제일 높은것을 고른다.
            max = dy[j]
    dy[i] = max + arr[i][1] # 가능한 것 중 가장 높이 쌓아올린 것에 자신을 더한다.
    if res < dy[i] :
        res = dy[i]
    print(max, dy[i])
print(res)
'''

# answer.
'''
이건 수열문제가아니다. 입력받은 벽돌의 순서를 마음껏 바꿔도도된다.
조건은 밑면의 넓이, 무게다.
먼저, 밑면의 넓이가 넓은순대로 정렬한다. => 더이상 밑면의 넓이 조건은 볼 필요가 없다.
이제 무게만 따져서 쌓아올려가면된다.
'''

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort(key = (lambda x:x[0]), reverse= True) # 여기만 다름!!!!!밑면의 넓이가 넓은순대로 정렬한다. => 더이상 밑면의 넓이 조건은 볼 필요가 없다. 
arr.insert(0,0) 
dy = [0] * (n+1)
dy[1] = arr[1][1]
res = dy[1]


for i in range(2, n+1):
    max = 0
    for j in range(i-1,0,-1):
        if arr[i][2] < arr[j][2] and max < dy[j] :
            max = dy[j]
    dy[i] = max + arr[i][1] .
    if res < dy[i] :
        res = dy[i]
    print(max, dy[i])
print(res)
