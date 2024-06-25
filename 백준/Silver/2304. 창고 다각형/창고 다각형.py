N = int(input())
answer = 0
l = [list(map(int,input().split())) for _ in range(N)]
# 가장 높은 기둥 구하기
l.sort(key=lambda x:-x[1])
max_hight = l[0][1]
# x축 기준으로 정렬
l.sort()
# 가장 높은 기둥 인덱스 구하기
h_index = 0
for i in range(N):
    if l[i][1] == max_hight:
        h_index = i
start_x = l[0][0]
h = l[0][1]
for i in range(1,h_index+1):
    if l[i][1] >= h:
        answer += (l[i][0] - start_x) * h
        start_x = l[i][0]
        h = l[i][1]

start_x = l[N-1][0] +1
h = l[N-1][1]
for i in range(N-1,h_index-1,-1):
    if l[i][1] >= h:
        answer += (start_x-(l[i][0]+1)) * h
        start_x = l[i][0] +1
        h = l[i][1]

print(answer + l[h_index][1])