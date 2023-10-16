from itertools import product
def solution(word):
    answer = 0
    word_list = ["A","E","I","O","U"]
    wc = []
    wl = set()
    for i in range(1,6):
        wc += product(word_list,repeat = i)
    for j in wc:
        wl.add(''.join(j))
    wl = sorted(wl)
    answer = wl.index(word)+1
    return answer