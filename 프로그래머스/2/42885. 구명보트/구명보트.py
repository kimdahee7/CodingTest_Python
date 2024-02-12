from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    q = deque(people)
    while q:
        if len(q) == 1:
            answer +=1
            break
        if q[0] + q[-1] <= limit:
            answer +=1
            q.pop()
            q.popleft()
        else:
            answer+=1
            q.pop()
    return answer
