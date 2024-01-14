from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    l = [0] * bridge_length
    total = 0
    while truck_weights:
        answer += 1
        total -= l[0]
        l.pop(0)
        if total + truck_weights[0] <= weight:
            total += truck_weights[0]
            l.append(truck_weights.pop(0))
        else:
            l.append(0)
    answer += bridge_length
    return answer