N,M = map(int,input().split())
word_list = [input() for _ in range(N)]
word_list.sort()
word_list.sort(key=len,reverse=True)
memorize_list = {}
for w in word_list:
    if len(w) >= M:
        if w not in memorize_list:
            memorize_list[w] =1
        else:
            memorize_list[w] += 1
memorize_list = sorted(memorize_list, key=lambda x:-memorize_list[x])

for m in memorize_list:
    print(m)