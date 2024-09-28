while True:
    try:
        n = int(input())
        k = 1
        count = 1
        while True:
            if k % n == 0:
                print(count)
                break
            else:
                k = k * 10 + 1
                count +=1
    except EOFError:
        break
