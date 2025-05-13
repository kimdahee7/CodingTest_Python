N = int(input())

l = []
def back():
    if len(l) == N:
        for num in l:
            print(num, end=" ")
        print()
        return
    for i in range(1, N + 1):
        if i not in l:
            l.append(i)
            back()
            l.pop()
back()