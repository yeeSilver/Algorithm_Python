'''
브론즈2) https://www.acmicpc.net/problem/2577

1) 자릿수가 고정되어있지 않은 숫자의 각 자리의 수를 구해야 할 때
숫자 -> str 으로 변환한 뒤에 배열에 넣기 -> ['1', '2', ...] 이런 식으로 저장됨.

2) count함수 : 
  - 배열.count('찾고자하는 문자')
  - 문자열.count('찾고자하는 문자')

Q) 문득 궁금해진 점.
  입력 코드를 여러번 쓰는 것 vs 배열을 더 쓰는 것
  --내코드--
  arr = []*3
  for i in range(3):
      arr[i] = int(input())


  --타인코드--
  a = int(input())
  b = int(input())
  c = int(input())

  

'''
arr = []*3
for i in range(3):
    arr[i] = int(input())


# 숫자를 문자열로 변환하고 배열에 원소로 넣으면 한 글자씩 분리되어 str으로 들어가게 됨

# -- 수정 전 코드 --
# mul = arr[0] * arr[1] * arr[2]
# seperate = []
# for i in str(mul):
#     seperate.append(i)

# -- 수정 후 코드 --
mulNum = list(str(arr[0]*arr[1]*arr[2]))
for i in range(10):
    print(mulNum.count(i))
