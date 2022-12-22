# 중앙값계산2

n = int(input())
arr = list(map(int, input().split()))
sortedarr = []

for i in range(n):
    sortedarr.append(arr[i])
    if (i % 2 == 0):
        sortedarr.sort()
        print(sortedarr[i//2], end=" ")
