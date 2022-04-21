# 1000번 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오. 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

# ---- 에러 코드 ----
# a, b = int(input('정수 A, B를 입력해주세요').split())
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'

# ---- 수정 코드 : 틀렸습니다 ----
# map(적용할 함수, 순회 가능한 객체)
# a, b = map(int, input('정수 A, B를 입력해주세요 (0 < A, B < 10)').split())
# print(a+b)

# ---- 수정 코드 : 맞았습니다 ----
a, b = map(int, input().split())
print(a+b)

# ---- 수정 코드 : 맞았습니다 ----
a, b = input().split()
a = int(a)
b = int(b)
print(a+b)

# 1001번 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
a, b = map(int, input().split())
print(a-b)
