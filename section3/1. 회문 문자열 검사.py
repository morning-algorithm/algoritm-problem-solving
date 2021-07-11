import sys
#sys.stdin=open("input.txt", "rt")

n=int(input())
a=[1]*n
s=[]
for i in range(n):
    s=input()
    for j in range(int(len(s)/2)):
        if s[j]==s[len(s)-1-j]:
            continue
        elif ord(s[j])>=97 and ord(s[len(s)-1-j])==ord(s[j])-32:
            continue
        elif ord(s[j])<=90 and ord(s[len(s)-1-j])==ord(s[j])+32:
            continue
        else:
            a[i]=0
            break
    if a[i]==0:
        print("#",i+1,sep="",end=" ")
        print("NO")
    else:
        print("#",i+1,sep="",end=" ")
        print("YES")