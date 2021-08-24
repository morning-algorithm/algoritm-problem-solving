'''
### 병합정렬
    * 분할정복
    * D(0,7) => lt, rt를 절반으로 나누는 작업 일어남. 
    * 후위순회 !!!!!!!!!!!!!!!!
    
###


'''
def Dsort(lt, rt): 
    if lt<rt: # 원소가 하나가 되면 여기에 걸려서 끝남. 정렬 완료라고 본다.
        
        mid = (lt+rt) // 2 
        Dsort(lt, mid) # 왼쪽자식 끝나고 (다 정렬되고)
        Dsort(mid+1, rt) # 오른쪽자식 끝나고 (다 정렬되고)
        
        ####### 본연의 일 (합친다) #######

        # 왼쪽자료, 오른쪽 자료의 원소를 비교해가며 합친다 (사실 이때 정렬됨) 
        p1 = lt #왼쪽 자료의 제일 작은 인덱스
        p2 = mid+1 #오른쪽 자료의 제일 작은 인덱스
        tmp = []
        while p1 <= mid and p2<=rt: #왼쪽자료나 오른쪽 자료의  제일 큰 인덱스
            if arr[p1]<arr[p2]:
                tmp.append(arr[p1])
                p1+=1
            else:
                tmp.append(arr[p2])
                p2+=1

        #한쪽이 먼저 다 끝난경우 나머지 남은 것은 그냥 싹 넣어버린
        if p1<= mid: #p2가 먼저 끝난경우
            tmp = tmp+arr[p1:mid+1]
        if p2 <= rt:            
            tmp = tmp+arr[p2:rt+1]

        #현재 D(4,7)이면 만들어진 tmp0~4를 arr4~7에 넣어야함. 
        for i in range(len(tmp)):
            arr[lt + i] = tmp[i]
            
        ###################################
