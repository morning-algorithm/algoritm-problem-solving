import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
score = list(map(int, input().split()))

ave = (sum(score)/n)+0.5
ave = int(ave)
min = abs(score[0]-ave)
index = 0

for i in range(1, len(score)):
    r = abs(score[i]-ave)
    if r < min:
        min = r
        index = i
    elif r == min:
        if score[i] > score[index]:
            index = i

print(score[index], index+1)