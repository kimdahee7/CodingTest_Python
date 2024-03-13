def solution(elements):
    answer = set()
    n = len(elements)
    elements.extend(elements[0:n-2])
    for i in range(n):
        for j in range(i+1,i+n+1):
            answer.add(sum(elements[i:j]))
    return len(answer)
