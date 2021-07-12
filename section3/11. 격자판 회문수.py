board = [list(map(int, input().split())) for _ in range(7)]

result = 0
for i in range(3):
    for j in range(7):
        # 가로 검사
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            result += 1

        # 세로는 일일이 회문 검사
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            result += 1

print(result)
