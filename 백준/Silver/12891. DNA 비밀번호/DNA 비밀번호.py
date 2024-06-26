import sys
input = sys.stdin.readline
S,P = map(int,input().split())
dna = input()
a,c,g,t = map(int,input().split())
window = dna[0:P]
dic = {"A":0,"C":0,"G":0,"T":0}
for i in window:
    dic[i] +=1
if dic["A"] >= a and dic["C"] >= c and dic["T"] >= t and dic["G"] >= g:
    answer = 1
else:
    answer = 0
start = 0
for i in range(P,S):
    if dna[i] == "A":
        dic["A"] +=1
    elif dna[i] == "C":
        dic["C"] +=1
    elif dna[i] == "G":
        dic["G"] +=1
    elif dna[i] == "T":
        dic["T"] +=1
    if dna[start] == "A":
        dic["A"] -=1
    elif dna[start] == "C":
        dic["C"] -=1
    elif dna[start] == "G":
        dic["G"] -=1
    elif dna[start] == "T":
        dic["T"] -=1
    start +=1
    if dic["A"] >=a and dic["C"] >=c and dic["T"] >=t and dic["G"] >=g:
        answer +=1
print(answer)