import sys
#sys.stdin=open("input.txt", "r")

n=int(input())
meeting=[]
for i in range(n):
    s, e=map(int, input().split())
    meeting.append((e, s))
    
meeting.sort()
end=0
count=0

for e, s in meeting:
    if s>=end:
        end=e
        count+=1
        
print(count)
