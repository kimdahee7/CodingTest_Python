def solution(wallet, bill):
    answer = 0
    while True:
        wallet.sort()
        bill.sort()
        if wallet[1] >= bill[1] and wallet[0] >= bill[0]:
            return answer
        else:
            bill[1] = bill[1] // 2
            answer +=1