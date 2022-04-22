''' 실버 5 !! 첫 실버 문제드앙!
4673) https://www.acmicpc.net/problem/4673
셀프 넘버 = 생성자가 없는 숫자 (즉 어떤 숫자를 조합해서 만들어진 수가 아닌 것.)

1 1 2
2 2 4
3 3 6
4 4 8
5 5 10
6 6 12
7 7 14
8 8 16
9 9 18
10 -> 1 0 10 : 11
11 -> 1 1 11 : 13
12 -> 1 2 12 : 15

1 
3 
5 
7 
9 
20
31
42
53
64
75
86
97
셀프넘버인지 유무 파악이 되야 함. 
일단 예를들면, d(75) = 7 + 5 + 75 = 87

1. 모든 수를 돌려서 리스트에 넣고 (중복 안되게) 거기에 없는 수를 출력
2. 해당 수가 생성자가 있는 지 검사하는 함수 만들기

// : 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함




'''
result = []
array = []


def solution(n):
    answer = 0
    while n > 0:
        answer += n % 10
        n //= 10  # n=n//10(n을 10으로 나눈 뒤 몫의 정수만 다시 가져와)
    return answer


for i in range(1, 10000):
    num = solution(i) + i
    if (num <= 10000):
        result.append(num)

for j in range(1, 10000):
    if j not in result:
        if j not in array:
            array.append(j)

array.sort()
for k in array:
    print(k)
