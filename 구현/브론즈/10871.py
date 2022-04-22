'''
10871) 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

정수형 배열 받기 -> inputList = list(map(int, input().split()))
개행 없이 출력 -> end='' 
파이썬은 end에 \n이 지정된 상태가 디폴트값인데 end에 빈 문자열을 지정해주면 \n 상태가 제거된다. 
'''
n, x = map(int, input().split())
sequence = list(map(int, input().split()))
result = []
for i in sequence:
    if i < x:
        result.append(i)

for i in result:
    print(i, end=' ')
