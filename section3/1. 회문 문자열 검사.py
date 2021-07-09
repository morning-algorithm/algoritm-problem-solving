import sys
#sys.stdin = open("input.txt","rt")

#me
N = int(input())

for n in range(N):
	s = input().lower()
	if s == s[::-1]:
		print(f"#{n+1} YES")
	else:
		print(f"#{n+1} NO")

		

'''answer
코딩인터뷰에서는 직접 구현하는 것도 중요!

가운데를 기준으로 대칭이므로 //2
for i in range (len(s) // 2):
        if s[j] != s[-j-1]:
                회문아님
                break
else:
        회문
'''
