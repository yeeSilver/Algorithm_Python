'''
11022) 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다.

이중 배열 받는 연습을 더 하자!

'''
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    print('Case #%d: %d + %d = %d' %
          (i+1, arr[i][0], arr[i][1], arr[i][0]+arr[i][1]))
