
def DFS(idx, P):
    global count
    if idx==n:
        count+=1
        for j in range(P):
            print(chr(out[j]+64), end='')
        print()
    else:
        for i in range(1, 27):
            if code[idx]==i: # 한자리
                out[P]=i
                DFS(idx+1, P+1)
            elif i>=10 and code[idx]==i//10 and code[idx+1]==i%10: # 두자리
                out[P]=i
                DFS(idx+2, P+1)
                
code = list(map(int, input()))

n = len(code)
count = 0
code.insert(n, -1)
out = [0]*(len(code))
DFS(0, 0)

print(count)

