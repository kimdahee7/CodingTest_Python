N = int(input())
A = list(map(int,input().split()))
c = list(map(int,input().split()))

answer = []

def backtracking(index,result):
    if index == N:
        answer.append(result)
        return
    else:
        if c[0] > 0:
            c[0] -=1
            backtracking(index+1,result+A[index])
            c[0] +=1
        if c[1] > 0:
            c[1] -=1
            backtracking(index+1, result-A[index])
            c[1] +=1
        if c[2] > 0:
            c[2] -=1
            backtracking(index+1, result*A[index])
            c[2] +=1
        if c[3] > 0:
            c[3] -=1
            if result < 0:
                backtracking(index+1, -(-result // A[index]))
            else:
                backtracking(index+1,result // A[index])
            c[3] +=1

backtracking(1,A[0])
print(max(answer))
print(min(answer))