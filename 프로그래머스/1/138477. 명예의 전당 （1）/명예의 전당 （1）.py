import heapq
def solution(k, score):
    answer = []
    l = []
    for i in score:
        if len(l) == k and l[0] < i:
            heapq.heappop(l)
            heapq.heappush(l,i)
            answer.append(l[0])
        elif len(l) == k and l[0] >= i:
            answer.append(l[0])
        else:
            heapq.heappush(l,i)
            answer.append(l[0])
    return answer