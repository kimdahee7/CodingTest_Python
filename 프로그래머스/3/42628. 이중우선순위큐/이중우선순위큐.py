import heapq
def solution(operations):
    l1 = []
    for i in operations:
        if i[0] == "I":
            heapq.heappush(l1,int(i[2:len(i)]))
        elif len(l1) == 0:
             continue
        elif i == "D -1":
            heapq.heappop(l1)
        else:
            l2 = []
            while len(l1) > 1:
                heapq.heappush(l2,heapq.heappop(l1))
            heapq.heappop(l1)
            l1 = l2
    if len(l1) == 0:
        return [0,0]
    else:
        return [max(l1),min(l1)]