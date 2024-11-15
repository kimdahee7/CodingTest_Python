import heapq

T = int(input())
for _ in range(T):
    k = int(input())
    min_h = []
    max_h = []
    dic = {}
    for _ in range(k):
        a,b = map(str,input().split())
        if a == "I":
            if int(b) not in dic:
                dic[int(b)] = 1
            else:
                dic[int(b)] +=1
            heapq.heappush(min_h,int(b))
            heapq.heappush(max_h,-int(b))
        # 최솟값을 삭제해야하는 경우
        elif a == "D" and b == "-1":
            cnt = 0
            while cnt < 1:
                if len(min_h) == 0:
                    break
                if dic[min_h[0]] == 0:
                    heapq.heappop(min_h)
                else:
                    k = heapq.heappop(min_h)
                    dic[k] -= 1
                    cnt +=1
        # 최댓값을 삭제해야하는 경우
        else:
            cnt = 0
            while cnt < 1:
                if len(max_h) == 0:
                    break
                if dic[-max_h[0]] == 0:
                    heapq.heappop(max_h)
                else:
                    k = heapq.heappop(max_h)
                    dic[-k] -= 1
                    cnt += 1
    answer = []
    for i in dic:
        if dic[i] != 0:
            answer.append(i)
    if len(answer) == 0:
        print("EMPTY")
    else:
        print(max(answer),min(answer))
