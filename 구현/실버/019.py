'''
1316) 실버5 https://www.acmicpc.net/problem/1316
arr는 입력받은 문자의 배열을 알파벳 단위로 쪼개서 넣은 배열
result는 arr를 하나씩 검수하고 통과할 때 append해주는 배열

1) 첫번째 두번째 -> 아묻따 result.append
2) 3번쨰 부터 비교
  A) arr가 1,2 자리 일때는 아묻따 true
  B) arr의 len이 3 이상일 때
    a) arr[i]가 result에 있다면
      if) s[i-1] == s[i]:
        result에 append
      else) s[i-1] != s[i]:
        pass
      (result arrya에 넣지 말기)
      
    b) 해당 문자가 result에 없는 경우 겹치는 것이 나오지 않은 경우: 아묻따 apeend

'''

from operator import truediv
from pickle import FALSE, TRUE


n = int(input())
answer = [0] * n

for i in range(n):
    answer[i] = input()


def groupNum(arr):
    result = []
    if(len(arr) == 1 or len(arr) == 2):
        r = True
    else:
        result.append(arr[0])
        result.append(arr[1])
        for i in range(2, len(arr)):
            if arr[i] in result:
                if arr[i-1] == arr[i]:
                    result.append(arr[i])
                else:
                    pass
            else:
                result.append(arr[i])

        if len(arr) == len(result):
            r = True
        else:
            r = False
    return r


s = []
groupnumber = 0
for i in answer:
    for j in i:
        s.append(j)

    if (groupNum(s) == True):
        groupnumber += 1
    s = []

print(groupnumber)
