import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()
k = ""
total_n = N + N+1
for i in range(1,total_n+1):
    if i%2 != 0:
        k += "I"
    else:
        k += "O"
answer = 0
for i in range(M-total_n+1):
    if S[i:i+total_n] == k:
        answer +=1

print(answer)