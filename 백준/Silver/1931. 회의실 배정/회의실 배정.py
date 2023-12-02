N = int(input())
l= [tuple(map(int,input().split())) for _ in range(N)]
l.sort(key=lambda x:(x[1],x[0]))
limit = l[0][1]
count = 1
for i in range(1,len(l)):
   if limit <= l[i][0]:
     count +=1
     limit = l[i][1]
print(count)