from itertools import combinations
L,C = map(int,input().split())
word_list = set(list(map(str,input().split())))
aeiou = ["a","e","o","i","u"]

perm = combinations(word_list,L)
answer = set()
for i in perm:
    cnt_a = 0
    cnt_b = 0
    i = sorted(i)
    for j in i:
        if j in aeiou:
            cnt_a +=1
        else:
            cnt_b +=1
    if cnt_a >=1 and cnt_b >=2:
        answer.add("".join(i))
answer = sorted(answer)
for i in answer:
    print(i)
