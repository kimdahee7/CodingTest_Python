import sys
input = sys.stdin.readline

p,m = map(int,input().split())
room = []
for _ in range(p):
  level,n = map(str,input().split())
  level = int(level)
  if len(room) == 0:
    room.append([(level,n)])
  else:
    check_in = False
    for i in room:
      if i[0][0] -10 <= level <= i[0][0] +10 and len(i) < m:
        i.append((level,n))
        check_in = True
        break
    if not check_in:
      room.append([(level,n)])

for r in room:
  r.sort(key=lambda x:x[1])
for r in room:
  if len(r) == m:
    print("Started!")
  else:
    print("Waiting!")
  for i in r:
    print(i[0],i[1])