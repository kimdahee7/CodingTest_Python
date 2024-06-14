S = input()
N = len(S)

a_total_count = S.count("a")
b_total_count = N-a_total_count
start = 0
end = a_total_count -1

window = S[start:end+1]
a_count = window.count("a")
b_count = window.count("b")
answer = 1e9
while start < N:
    if b_count <= a_total_count-a_count:
        answer = min(answer,b_count)
    if S[start] == "a":
        a_count -=1
    else:
        b_count -=1
    if S[(end+1)%N] == "a":
        a_count +=1
    else:
        b_count +=1
    end +=1
    start +=1

print(answer)