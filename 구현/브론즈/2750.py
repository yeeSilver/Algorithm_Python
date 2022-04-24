'''
2750) N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

list.sort() : 오름차순 정렬
list.sort(reverse=False) :오름차순
list.sort(reverse=True) : 내림차순
'''

n = int(input())
number = []

for i in range(n):
    number.append(int(input()))

number.sort()
for i in (number):
    print(i)
