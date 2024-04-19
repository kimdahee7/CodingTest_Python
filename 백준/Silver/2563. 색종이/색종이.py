N = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(N):
    x, y = map(int, input().split())

    for i in range(x,x+10):
        for j in range(y,y+10):
            paper[j][i] = 1
answer = 0
for i in range(100):
    answer += paper[i].count(1)
print(answer)