import sys
#sys.stdin=open("input.txt", "r")

nList = [list()]*9

for i in range(len(nList)):
    nList[i] = list(map(int, input().split()))

correct = True

for i in range(len(nList)):
    chH = [0]*10
    chV = [0]*10

    for j in range(len(nList)):
        if(chH[nList[i][j]] != 1):
            chH[nList[i][j]] = 1
        elif(chH[nList[i][j]] == 1):
            correct = False
            break;

        if(chV[nList[j][i]] != 1):
            chV[nList[j][i]] = 1
        elif(chV[nList[j][i]] == 1):
            correct = False
            break;

    if correct == False:
            break;


for i in range(3):
    for j in range(3):
        ch=[0]*10
        for k in range(3):
            for s in range(3):
                if(ch[nList[i*3+k][j*3+s]] != 1):
                    ch[nList[i*3+k][j*3+s]] == 1
                elif(ch[nList[i*3+k][j*3+s]] == 1):
                    correct = False
                    break;
                
        if correct == False:
            break;

if correct:
    print("YES")
else:
    print("NO")
                
