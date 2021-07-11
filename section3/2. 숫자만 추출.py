import sys
#sys.stdin=open("input.txt", "rt")

s=input()
n=0

for i in range(len(s)):
    if ord(s[i])>=48 and ord(s[i])<=57:
        n*=10
        n+=(ord(s[i])-48)

cnt=0
for i in range(1,n+1):
    if n%i==0:
        cnt+=1

print(n)
print(cnt)