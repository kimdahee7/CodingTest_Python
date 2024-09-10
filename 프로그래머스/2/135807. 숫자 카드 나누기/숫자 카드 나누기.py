import math
def solution(arrayA, arrayB):
    answer = 0
    x1 = arrayA[0]
    x2 = arrayB[0]
    # 조건 1확인 
    for i in range(len(arrayA)):
        x1 = math.gcd(x1,arrayA[i])
    if checkarray(x1,arrayB):
        answer = max(answer,x1)   

    # 조건 2확인 
    for i in range(len(arrayB)):
        x2 = math.gcd(x2,arrayB[i])
    if checkarray(x2,arrayA):
        answer = max(answer,x2)
    return answer

def checkarray(x,array):
    for i in array:
        if i % x == 0:
            return False
    return True