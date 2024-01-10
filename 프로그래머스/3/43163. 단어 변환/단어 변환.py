from collections import deque
def solution(begin, target, words):
    answer = 0
    visited = [False] * len(words)
    q = deque()
    q.append((begin,0))
    while q:
        x,total = q.popleft()
        if x == target:
            answer = total
            break
        for i in range(len(words)):
            count = 0
            if not visited[i]:
                for a in range(len(x)):
                    if x[a] != words[i][a]:
                        count +=1
                if count == 1:
                    q.append((words[i],total+1))
                    visited[i] = True
            
    return answer