import sys
sys.stdin=open("input.txt", "rt")

# 아나그램 - 두 문자열이 알파벳의 나열 순서는 다르지만 구성이 일치하는 것
#정답 풀이3: C언어식 풀이
a=input()
b=input()
str1=[0]*52#A~Z:65~90(26), a~z:97~122(26)
str2=[0]*52
for x in a:
    if x.isupper():
        str1[ord(x)-65]+=1
    else:
        str1[ord(x)-71]+=1
for x in b:
    if x.isupper():
        str2[ord(x)-65]+=1
    else:
        str2[ord(x)-71]+=1
for i in range(52):
    if str1[i]!=str2[i]:
        print("NO")
        break
else:
    print("YES")


''' 정답 풀이2: 딕셔너리 개선된 코드 
a= input()
b=input()

sH=dict()#딕셔너리 선언
for x in a:
    sH[x]=sH.get(x,0)+1
for x in b:
    sH[x]=sH.get(x,0)-1

for x in a:
    if sH.get(x)>0:
        print("NO")
        break
else:
    print("YES")
'''

'''정답 풀이1: 딕셔너리
a= input()
b=input()

str1=dict()#딕셔너리 선언
str2=dict()
for x in a:
    str1[x]=str1.get(x,0)+1#str1에 x라는 키가 없으면 생성한 후 값으로 0 대입 #str1[x]+1
for x in b:
    str2[x]= str2.get(x,0)+1

for i in str1.keys():
    if i in str2.keys():
        if str1[i]!=str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
'''
''' 내 풀이
s1=list(input())
s2=list(input())

s1.sort()
s2.sort()

if s1==s2:
    print("YES")
else:
    print("NO")
'''