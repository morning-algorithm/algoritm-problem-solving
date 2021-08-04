import sys
#sys.stdin=open("input.txt", "r")
#알파코드 DFS
def DFS(s):# s는 start point
    global cnt
    if s>=len(c):
        for x in res:
            print(x, end="")
        print()
        cnt+=1
        return
    else:
        if s+1<=len(c):
            if int(c[s])==0:# 0 예외 처리
                return
            res.append(alphabet[int(c[s:s+1])-1])
            DFS(s+1)
            res.pop()
        if  s+2<=len(c) and 1<=int(c[s:s+2])<=26:
            res.append(alphabet[int(c[s:s+2])-1])
            DFS(s+2)
            res.pop()


if __name__ =="__main__":
    c=input()
    res=[]# 알파 코드 결과
    alphabet=[chr(i+65) for i in range(26)]
    cnt=0
    DFS(0)
    print(cnt)