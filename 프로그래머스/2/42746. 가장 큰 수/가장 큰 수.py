def solution(numbers):
    numbers = list(map(str, numbers))
    # 원소가 1000이하 이므로 원소를 (*3)3자리까지 늘려서 비교 
    numbers.sort(key=lambda x: x * 3, reverse= True)
    # 원소가 0일 경우 00 또한 0으로 반환해야 하기 때문에 int 변환 후 다시 str 변환
    return str(int(''.join(numbers)))