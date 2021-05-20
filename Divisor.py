"""
과제 번호 : 02_1
문제 내용 : 주어진 임의의 0보다 큰 정수에 대한 약수들을 리스트로 반환하는 함수 divisors()를 정의해라.
"""
def divisors(n):
    i = 1
    div = []

    while i <= n:
        if n%i == 0:
            div += [i]
        i += 1
    return div


"""
과제 번호 : 02_2
문제 내용 : 키보드를 통해 0보다 큰 정수를 입력받아 약수를 리스트로 출력해주는 프로그램을 작성해라.
          (단, -1이 입력될 때까지 이를 반복하라.)
"""

if __name__=='__main__':
    n = int(input('정수를 입력하시오(-1 : 종료) : '))

    while n != -1:
        divisors_n = divisors(n)
        print(f'{n}의 약수 : {divisors_n}')

        n = int(input('정수를 입력하시오(-1 : 종료) : '))
    print("종료합니다.")
