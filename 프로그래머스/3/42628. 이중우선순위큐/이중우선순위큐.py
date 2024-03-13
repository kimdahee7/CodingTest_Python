import heapq
def solution(operations):
    answer = []
    l = []
    for i in operations:
        print(l)
        a,b = i.split()
        if a == "I":
            heapq.heappush(l,int(b))
        elif a == "D" and b == "-1":
            if len(l) != 0:
                heapq.heappop(l)
        else:
            if len(l) == 1:
                heapq.heappop(l)
            else:
                l2 = []
                while len(l) > 1:
                    x = heapq.heappop(l)
                    heapq.heappush(l2,x)
                l = l2
    if len(l) == 0:
        answer = [0,0]
    else:
        answer = [max(l),min(l)]
    return answer