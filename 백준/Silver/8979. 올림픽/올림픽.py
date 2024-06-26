import sys
input = sys.stdin.readline
N,K = map(int,input().split())
l = [list(map(int,input().split())) for _ in range(N)]
l.sort(key=lambda x:-x[3])
l.sort(key=lambda x:-x[2])
l.sort(key=lambda x:-x[1])
answer_list = [(l[0][0],1)]
answer = 1
g = l[0][1]
s = l[0][2]
b = l[0][3]
for i in range(1,N):
    if l[i][1] == g and l[i][2] == s and l[i][3] == b:
        answer_list.append((l[i][0],answer))
    else:
        answer +=1
        g = l[i][1]
        s = l[i][2]
        b = l[i][3]
        answer_list.append((l[i][0],answer))
for i in answer_list:
    if i[0] == K:
        print(i[1])
        exit()