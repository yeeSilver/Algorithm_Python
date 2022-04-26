'''
10952) https://www.acmicpc.net/problem/10952
A+B를 출력하는 프로그램. 입력의 마지막에는 0 두 개가 들어온다.
'''

while (True):
    a, b = map(int, input().split())
    if (a == 0 and b == 0):
        break
    print(a+b)

# 한꺼번에 다 입력받고 출력하기
'''
result = []
while (True):
    a, b = map(int, input().split())
    if (a == 0 and b == 0):
        break
    result.append(a+b)
for i in result:
    print(i, end='\n')
'''
