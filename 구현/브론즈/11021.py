'''
문제) https://www.acmicpc.net/problem/11021
이중배열로 입력받고 저장하기 
  => arr = [list(map(int, input().split())) for _ in range(n)]

* for _ in range(n)
 : 인덱스가 필요하지 않을 때 언더스코어(_) 를 쓴다.
(참조 :https://sohee-dev.tistory.com/15)

* 에러 : TypeError: 'int' object is not subscriptable
for i in range(n):
    addNum = i[i][0] + i[i][1]
이 코드에서 에러가 남.
해당 에러는 인텍스를 갖지 않는 값에 인덱스를 가지게 코드를 짰을 경우 발생하는 에러라고 한다. 
'''
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# arr = []
# for i in range(n):
#     arr[i] = list(map(int, input().split()))

for i in range(n):
    addNum = arr[i][0] + arr[i][1]
    print('Case #%d: %d' % (i+1, addNum))
