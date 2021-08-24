#병합정렬

def Dsort(lt, rt):
    if lt < rt:
        mid = (lt+rt) // 2
        Dsort(lt, mid)
        Dsort(mid+1, rt)
        p1 = lt
        p2 = mid+1
        tmp = []

        while p1 <= mid and p2 <= rt:
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1 += 1
            else:
                tmp.append(arr[p2])
                p2 += 1

        if p1 <= mid: #남은 값들 다 들어감
            tmp = tmp+arr[p1:mid+1]
        if p2 <= rt: #남은 값들 다 들어감
            tmp = tmp+arr[p2:rt +1]

        for i in range(len(tmp)):
            arr[lt+i] = tmp[i]
        
arr = [23, 11, 45, 36, 15, 67, 33, 21]
print(arr)
Dsort(0, 7)
print(arr)
