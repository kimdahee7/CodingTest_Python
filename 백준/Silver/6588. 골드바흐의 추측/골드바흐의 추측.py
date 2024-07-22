import math
arr = [True for i in range(1000001)]

for i in range(2,int(math.sqrt(1000000) +1)):
    if arr[i] == True:
        k = 2
        while i*k <= 1000000:
            arr[i*k] = False
            k +=1
answe = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        c = 0
        for i in range(2,n-1):
            if arr[i] == True and arr[n-i] == True:
                print(f"{n} = {i} + {n-i}")
                c +=1
                break
        if c==0:
            print("Goldbach's conjecture is wrong.")
            break