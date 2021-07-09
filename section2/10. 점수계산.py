import sys
#sys.stdin = open("input.txt","rt")

N = int(input())
l = map(int,input().split())

score = 0
sequence = 0
for item in l:
	if item == 0:
		sequence = 0
	else:
		sequence += 1
		score += sequence

print(score)