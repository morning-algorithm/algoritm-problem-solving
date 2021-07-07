
import sys
from collections import Counter 
sys.stdin = open("input.txt","rt")

#me
N = int(input())
r = list()
for n in range(N):
	l = list(map(int,input().split()))
	cl = Counter(l)
	same_cnt = max(cl.values())

	if same_cnt ==1 :
		r.append(max(cl.keys()) * 100)
	else:
		max_n = list(filter(lambda x:x[1] == same_cnt, cl.items()))
		if same_cnt == 2 :
			r.append(1000 + max_n[0][0] * 100)
		else: 
			r.append(10000 + max_n[0][0] * 1000)
print(max(r))

'''answer
먼저 abc값을 sorting해놓고 단순히 if문을 돌림
if a == b and b==c :
3개 눈 일치 
elif a == b or a == c :
2개 눈 일치
elif b == c : 
2개 눈 일치
else:
1개눈 일치 (정렬했으므로 c를 사용)
'''