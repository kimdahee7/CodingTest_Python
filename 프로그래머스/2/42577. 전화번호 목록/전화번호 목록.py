def solution(phone_book):
    phone_book.sort()
    n = len(phone_book)
    for i in range(n-1):
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            return False
            exit()
    return True