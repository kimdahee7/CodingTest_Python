import heapq
def solution(scoville, K):
    answer = 0
    h = []
    for i in scoville:
        heapq.heappush(h,i)
    while True:
        if h[0] >= K:
            break
        if len(h) == 1:
            answer = -1
            break
        else:
            f = heapq.heappop(h)
            s = heapq.heappop(h)
            heapq.heappush(h,f+(s*2))
            answer+=1
    return answer