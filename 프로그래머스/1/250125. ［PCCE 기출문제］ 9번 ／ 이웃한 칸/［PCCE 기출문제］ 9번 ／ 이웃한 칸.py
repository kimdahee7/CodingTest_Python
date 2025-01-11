def solution(board, h, w):
    answer = 0
    W = len(board[0])
    H = len(board)
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    mainColor = board[h][w]
    for i in range(4):
        nx = dx[i] + w
        ny = dy[i] + h
        if 0<=nx<W and 0<=ny<H and board[ny][nx] == mainColor:
            answer +=1
    return answer