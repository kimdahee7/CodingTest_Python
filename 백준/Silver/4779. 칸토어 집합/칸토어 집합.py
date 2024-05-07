global result
result = ""

def fun(N):
    global result
    if N == 1:
        result += "-"
        return
    N = N//3
    fun(N)
    result += " "*N
    fun(N)

while True:
    try:
        N = int(input())
        fun(3**N)
        print(result)
        result = ""
    except EOFError:
        break