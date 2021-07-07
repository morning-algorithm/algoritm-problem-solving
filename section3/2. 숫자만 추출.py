import sys
#sys.stdin = open("input.txt","rt")

#me
def factor_cnt(x): 
	cnt = 0
	for i in range(1,int(x ** 0.5) + 1):
		if x % i == 0:
			if x != i:
				cnt += 2
			else:
				cnt += 1
	return cnt

s = input()
str_n = ''.join(list(filter(str.isdigit,s))).lstrip('0')
n = int(str_n)
print(n)
print(factor_cnt(n))

'''answer
isdecimal()은 0~9까지의 숫자만 찾아줌
2²에서 ²는 특수문자 => isdigit() 함수와 isnumeric() 함수로는 True가 반환

<맨 앞자리 0을 제외한 숫자를 만드는 방법>
res = 0
for x in s:
	if x.isdecimal():
		res = res*10+int(x) 
'''