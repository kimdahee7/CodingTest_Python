from itertools import combinations
def solution(friends, gifts):
    answer = [0] * len(friends)
    dic = {}
    for i in friends:
        if i not in dic:
            dic[i] = [0] * len(friends)
    # 각 인덱스에 해당하는 친구에게 준 선물의 개수 
    for i in gifts:
        a,b = map(str,i.split())
        dic[a][friends.index(b)] += 1

    # 각 친구마다 다음달에 받을 선물의 개수 
    combi = combinations(friends,2)
    for a,b in combi:
        # 주고 받은 기록이 없거나 수가 같다면 
        if dic[a][friends.index(b)] == dic[b][friends.index(a)]:
            # a의 선물 지수 
            total_a = 0
            for i in dic:
                if i != a:
                    total_a += dic[i][friends.index(a)]
            a_gift_rate = sum(dic[a])-total_a
            # b의 선물 지수 
            total_b = 0
            for i in dic:
                if i != b:
                    total_b += dic[i][friends.index(b)]
            b_gift_rate = sum(dic[b])-total_b
            if a_gift_rate > b_gift_rate:
                answer[friends.index(a)] += 1
            elif a_gift_rate < b_gift_rate:
                answer[friends.index(b)] += 1
        # 주고 받은 기록이 있다면 
        else:
            if dic[a][friends.index(b)] > dic[b][friends.index(a)]:
                answer[friends.index(a)] += 1
            else:
                answer[friends.index(b)] += 1
    return max(answer)