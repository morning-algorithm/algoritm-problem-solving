
import sys
#sys.stdin=open("input.txt", "rt")

n=int(input())
a=[0]*n

for i in range(2,n+1):
	for j in range(i,n+1,i):
		if i==j : continue
		if j%i==0 :
			a[j-1]=1

cnt=0
for i in range(len(a)):
	if a[i]==0:
		cnt+=1
print(cnt-1)

#cnt=0
#s_cnt=0
#for i in range(1,n+1):
#	for j in range(1,i+1):
#		if i%j==0:
#			cnt+=1
#	if cnt==2:
#		s_cnt+=1
#	cnt=0

#print(s_cnt) 