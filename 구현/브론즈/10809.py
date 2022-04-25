'''
10809 ) https://www.acmicpc.net/problem/10809
알파벳 위치 찾기 문제

- 인덱스 반환 함수 : list.index(찾고자하는 문자나 수)
- 알파벳 리스트에 저장하는 방법
  1) alphabet = list('abcdefghijklmnopqrstuvwxyz')
  2) 아스키코드 활용
    alphabet = list(range(97,123))
    chr() : 아스키코드를 문자열로 변환

  --- 예시 코드 ---
  string = input()
  alphabet = list(range(97,123))
  for i in alphabet :
      print(string.find(chr(i)))

-find함수:
  string.find(찾고자하는 문자)
  string.find(찾고자하는 문자, 시작index, 끝index)

인덱스를 찾는 함수
  1) find() :
   없을 경우 -1 출력
   문자열만 - 사용 O
   리스트. 튜플, 자료형 - 사용X
   
  2) index() : 
  없을 경우 valueError 에러 출력
  문자열, 리스트, 튜플 자료형 - 사용 o
  딕셔너리 - 사용X
'''
from unittest import result


alphabet = list('abcdefghijklmnopqrstuvwxyz')
str = list(input())
result = []

for i in alphabet:
    if i in str:
        # result.append(str.index(i))
        print(str.index(i), end=" ")
    else:
        # result.append(-1)
        print(-1, end=" ")
