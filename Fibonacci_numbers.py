"""
과제 번호 : 01_1
문제 내용 : 지정된 개수의 항을 가지는 피보나치 수열을 리스트로 반환하는 함수 fibonacci_num()와
          주어진 임의의 수보다 작은 값들로 항이 구성된 피보나치 수열 리스트로 반환하는 함수 fibonacci_less()를 각각 정의하라.
"""

# 지정된 개수의 항을 가지는 피보나치 수열
def fibonacci_num(n):
    past = 0
    current = 1
    lst = [past, current]

    i = 0
    while i < n-2:
        next = past + current
        i = i+1

        past = current
        current = next
        lst += [next]
    return lst

# 주어진 임의의 수보다 작은 값들로 항이 구성된 피보나치 수열
def fibonacci_less(n):
    past = 0
    current = 1
    next = past + current
    list_less = [past, current, next]

    while next <= n:
        past = current
        current = next
        next = past + current

        list_less += [next]
    return list_less[:-1]


"""
과제 번호 : 01_2
문제 내용 : 정의된 함수를 사용하여 15개의 항을 가지는 피보나치 수열과
          200보다 작은 피보나치 항을 가지는 피보나치 수열 리스트를 각각 출력해라.
"""

# 15개의 항을 가지는 피보나치 수열
#  200보다 작은 피보나치 항을 가지는 피보나치 수열
if __name__=='__main__':
    num = 15
    print(f'{num}개의 항을 가지는 피보나치 수열 : {fibonacci_num(num)}')

    ran = 200
    print(f'{ran}보다 작은 피보나치 항을 가지는 피보나치 수열 : {fibonacci_less(ran)}')







