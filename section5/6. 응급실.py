import sys
#sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
wait = list(map(int, input().split()))
waitIdx = list(range(0, n+1))
print(waitIdx)
count = 0
'''
p = wait[m]
wait.sort(reverse = True)
idx = wait.index(p)


while wait[m] != 0:
       tmp = waitIdx.pop(0)
       print(tmp)
       if wait[tmp] == max(wait):
           count += 1
           wait[tmp] = 0
           if tmp == m:
               break;
       else:
           waitIdx.append(tmp)

print(count+1)
'''

Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q=deque(Q)
cnt=0
while True:
    cur=Q.popleft()
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            print(cnt)
            break


