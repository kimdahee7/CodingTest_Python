import heapq
def solution(scoville, K):
    answer = 0
    h = []
    for i in scoville:
        heapq.heappush(h,i)
    while True:
        if h[0] >= K:
            break
        elif len(h) < 2:
            answer = -1
            break
        else:
            a = heapq.heappop(h)
            b = heapq.heappop(h)
            heapq.heappush(h,a+b*2)
            answer +=1
    return answer