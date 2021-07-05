import sys
#sys.stdin=open("input.txt", "rt")

n, k=map(int, input().split())
card=list(map(int, input().split()))

result=set()
for i in range(0, len(card)):
    for j in range(i+1, len(card)):
        for l in range(j+1, len(card)):
            result.add(card[i]+card[j]+card[l])

result = list(result)
result.sort(reverse=True)
print(result[k-1])
        
    
