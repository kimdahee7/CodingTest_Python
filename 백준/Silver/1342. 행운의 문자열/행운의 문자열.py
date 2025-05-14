S = input()

luck = []
dic = {}
for s in S:
    if s not in dic:
        dic[s] = 1
    else:
        dic[s] += 1

global answer
answer = 0

def back(pre_char, dic, cnt):
    global answer
    if cnt == len(S):
        answer +=1
        return
    for d in dic:
        if dic[d] != 0 and d != pre_char:
            dic[d] -=1
            back(d,dic,cnt +1)
            dic[d] +=1

back("",dic,0)
print(answer)