import sys
#sys.stdin=open("input.txt", "rt")

def reverse(x):#자연수 뒤집기 함수
	a=[]
	res=0
	while x/10!=0:
		a.append(x%10)
		x=int(x/10)
	for i in range(len(a)):
		res+=a[i]
		if i!=len(a)-1:
			res=res*10
	return res
def isPrime(x):#소수 확인 함수
	cnt=0
	for i in range(1,x+1):
		if x%i==0:
			cnt+=1
	if cnt==2: 
		return True
	else : 
		return False

n=int(input())
a=list(map(int, input().split()))

for i in range(len(a)):
	a[i]=reverse(a[i])
	if isPrime(a[i]):
		print(a[i], end=" ")
