import sys
#sys.stdin = open("input.txt","rt")

#me
def reverse(r,h):
	for i in range(0, (h-r)//2 + 1):
		l[r+i],l[h-i] = l[h-i],l[r+i]

l = list(range(1,21))
for n in range(10):
	r,h = map(int,input().split())
	#배열은 0부터 시작하므로 -1씩 해준다
	reverse(r-1,h-1)
	
print(' '.join(map(str,l)))

'''answer
range((h-r+1)//2) 으로 살짝 다르지만 동일하게 동작
'''