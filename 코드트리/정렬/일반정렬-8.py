# k번쨰로 신기한 문자열
# 단어가 n개 주어졌을 때, 문자열 T로 시작하는 단어들 중 사전순으로 정렬했을 때의 k번째 문자열을 출력하는 프로그램을 작성해보세요.
# startswith('특정 문자열') : 특정 문자열로 시작하는 지 확인
n, k, t = (input().split())
n = int(n)
k = int(k) - 1
words = []
results = []
for i in range(n):
    a = input()
    words.append(a)

for i in (words):
    if i.startswith(t):
        results.append(i)
results.sort()

print(results[k])
