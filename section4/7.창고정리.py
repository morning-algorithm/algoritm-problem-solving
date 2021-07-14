import sys
sys.stdin = open("input.txt","rt")

#me
n = int(input())
a = list(map(int,input().split()))
a.sort(reverse = True)
cnt = int(input())
c = 0

while cnt>0:
    m = min(a[0] - a[1], a[-2] - a[-1])
    a[-1] += m+1 #둘의 차이 +1 해줘야 전달 받은 이후에도 차이가 생김차이가 생김
    a[0] -= m+1
    
    cnt -= m+1
    a.sort(reverse = True)
    

print(a[0]-a[-1])


#answer
'''단순히 가장 높은 곳-1 , 가장 낮은 곳+1, sort를 m회 반복'''