def count(capacity):
    cnt = 1
    sum = 0
    for x in music:
        '''
        조건) capacity = 13, music = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        1) sum = 1 -> 3 -> 6 -> 10 -> 15
            sum = 15+6 => cnt = 2, sum = 6
        2) sum = 6 -> 13
            sum = 13 + 8 => cnt=3, sum = 8
        3) sum = 8 -> 17

        => cnt = 3
        '''
        
        if sum+x > capacity: #용량 초과, 새로운 dvd 하나 저장
            cnt += 1
            sum = x # 새로운 dvd에 저
        else:
            sum += x

    return cnt
        
n, m = map(int, input().split())
music = list(map(int, input().split()))
maxx = max(music)
lt = 1
rt = sum(music)
result = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) <= m and mid >= maxx: #가장 긴 노래의 용량을 담을 수 있어야하므로 mid >= maxx
        print(mid, count(mid))
        result = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(result)
