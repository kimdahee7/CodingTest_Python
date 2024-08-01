from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
name_list = []
dic = {}
for i in range(N):
    name = input()
    name_list.append(len(name))
    if len(name) not in dic:
        dic[len(name)] = 0

window = deque()
for i in range(K+1):
    window.append(name_list[i])
    dic[name_list[i]] +=1
name_length = window[0]
answer = dic[name_length] - 1

for i in range(len(name_list)-1):
    dic[name_list[i]] -=1
    window.popleft()
    if i+K+1 < len(name_list):
        window.append(name_list[i+K+1])
        dic[name_list[i+K+1]] +=1
    name_length = window[0]
    answer += dic[name_length] -1
print(answer)
