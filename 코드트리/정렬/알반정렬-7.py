# 순서를 바꾸었을 떄 같은 단어인지 판별하기
# 두 개의 단어가 입력으로 주어질 때 두 단어에 속하는 문자들의 순서를 바꾸어 동일한 단어로 만들 수 있는지 여부를 출력하는 코드를 작성해보세요.

# permutations : 모든 조합 순열

from itertools import permutations

word_a = list(input())
n = len(word_a)
word_b = (input())
ans = []
combi = list(permutations(word_a, n))
for i in combi:
    word = ''.join(i)
    if (word == word_b):
        print('Yes')
        ans.append(1)
        break

if len(ans) != 1:
    print('No')
