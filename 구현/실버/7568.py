'''
7568) 
1. (x kg, y cm) (몸무게, 키)
2. A(x, y) B(p, q) -> if (x > p) and (y > q) : A덩치가 더 크다


* 2차원 배열 입력받기
https://dailylifeofdeveloper.tistory.com/132

* 2차 배열 정렬
a) 첫번째 인덱스에 대해서 정렬
  list.sort(key=lambda x:x[0])
b) 두번째 인덱스에 대해서 정렬
  lst.sort(key=lambda x: (x[0], -x[1]))
c) 0번째 1번째 인덱스 모두 고려 : sort

* 파이썬 줄바꿈 없이 프린트 출력
  print(내용, end =' ')

-> 내가 하려고 했던 방식은 배열을 너무 많이 사용해서 공간복잡도가 커진다. 따라서 이 문제는 브루트포스 알고리즘을 사용해서 전체 비교를 통해 비교하면 될 것 이다. 

*Brute Force 브루트 포스 완전탐색 :
  이차 배열을 모두 탐색(비교하기 위해)해야 할때는 이중 for문을 사용해서 다 찾아보기로 하자. 그렇지만 브루트포스는 시간복잡도가 크기 때문에 마냥 효율적이진 않다고 한다. ...?? 다시 유튜브로 통해 배워보도록 하자.

'''


num = int(input())

people = []
for i in range(num):
    people.append(list(map(int, input().split())))

for i in people:
    grade = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            grade += 1
    print(grade, end=' ')
'''
def grade(arr):
    grade = 1
    result = []
    arr.sort(reverse=True)
    for i in range(len(arr)-1):
        if(arr[i][1] > arr[i+1][1]):
            result.append(grade)
            grade = i+1
        else:
            result.append(grade)
    result.append(len(arr))
    return result


result = grade(input)
for i in result:
    print(i, end=' ')
'''
