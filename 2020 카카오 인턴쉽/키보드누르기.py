def solution(numbers, hand):
    answer = ''
    
    position = [(3,1), (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)] 
    left = [1, 4, 7]
    right = [3, 6, 9]
    
    lh = (3, 0)
    rh = (3, 2)
    
    for n in numbers:
        if n in left:
            answer+= 'L'
            lh = position[n]
        elif n in right:
            answer+= 'R'
            rh = position[n]
        else:
            ld = abs(lh[0] - position[n][0]) + abs(lh[1] - position[n][1])
            rd = abs(rh[0] - position[n][0]) + abs(rh[1] - position[n][1])
            if ld < rd :
                answer += 'L'
                lh = position[n]
            elif ld == rd:
                if hand == 'right':
                    answer+= 'R'
                    rh = position[n]
                else:
                    answer += 'L'
                    lh = position[n]  
            else:
                answer+= 'R'
                rh = position[n]
                    
    return answer
