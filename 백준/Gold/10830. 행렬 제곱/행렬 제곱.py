N,B = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(N)]

# 행렬의 거듭제곱 구하는 함수
def square(A,B):
    answer = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            s = 0
            for k in range(N):
                s += A[i][k] * B[k][j]
                answer[i][j] = s % 1000
    return answer

# 분할 정복 
def divide(B,map):
    if B == 1:
        return map
    tmp = divide(B//2,map)
    if B % 2 == 0:
        return square(tmp,tmp)
    else:
        return square(square(tmp,tmp),map)

result = divide(B,map)
for i in result:
    for j in i:
        print(j%1000, end=" ")
    print()