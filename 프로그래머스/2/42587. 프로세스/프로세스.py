from collections import deque
def solution(priorities, location):
    answer = 0
    l = deque()
    for i in range(len(priorities)):
        l.append((i,priorities[i])) 
    priorities.sort(reverse=True)
    while True:
        if l[0][1] == priorities[0]:
            answer +=1
            if l[0][0] == location:
                return answer
            l.popleft()
            priorities.pop(0)
        else:
            l.append(l.popleft())
