n, m = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
#my code
#print(num.index(m) + 1)

lt = 0
rt = n-1

while lt <= rt :
    mid = (lt + rt) // 2
    if num[mid] == m:
        print(mid + 1)
        break
    elif num[mid] > m:
        rt = mid-1
    else:
        lt = mid+1
