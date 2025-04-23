H,W = map(int,input().split())
h = list(map(int,input().split()))

total = 0
for i in range(1,W-1):
    height = min(max(h[0:i+1]) , max(h[i:W]))
    total += height - h[i]
print(total)