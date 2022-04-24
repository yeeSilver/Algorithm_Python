'''
1157) 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

대소문자를 구분하지 않는 방법
- lower(), upper(), casefold() : 메서드를 사용한 대소문자를 구분하지 않는 문자열 비교
  lower() : 문자열을 소문자로 변환한 다음에 비교
  upper() : 문자열을 대문자로 변환한 다음에 비교
  casefold()는 위험하다... ?

set : 
  중복 X, 중복을 제거하기 위한 필터로 종종 쓰인다.
  순서 X -> 인덱스를 쓰고 싶다면? 인덱싱으로 접근하려면 다음과 같이 리스트나 튜플로 변환한후 해야 한다.
  set(배열)

'''

str = input().upper()
noDuplicate = list(set(str))
countList = []

for i in (noDuplicate):
    countList.append(str.count(i))

maxCount = max(countList)
if countList.count(maxCount) > 1:
    print('?')
else:
    print(noDuplicate[countList.index(maxCount)])
