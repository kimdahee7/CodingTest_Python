N = int(input())
dist = list(map(int,input().split()))
price = list(map(int,input().split()))
answer = dist[0] * price[0]
for i in range(2,N):
    if price[i-1] > price[i-2]:
        answer += dist[i-1] * price[i-2]
    else:
        answer += dist[i-1] * price[i-1]
print(answer)