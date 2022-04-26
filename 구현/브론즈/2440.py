'''
2440) 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

숫자를 거꾸로 출력하기
1) for문
  range([start], stop, [step])
  for i in range(n, 0, -1)
  
2) reversed() : 리스트이 원소를 거꾸로 뒤집고 반환
  for i in reversed(range(n))

문자열 거꾸로 출력하기
1) for문 
2) reverse
3) [::-1]

'''

n = int(input())
for i in range(n, 0, -1):
    print('*'*i)
