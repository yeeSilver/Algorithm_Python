'''
2309) 난쟁이 문제
'''
arr = []
result = []
for i in range(9):
    arr.append(int(input()))

hobbit = sum(arr) - 100

'''
for i in arr:
    for j in arr:
        if(i != j):
            if(i+j == hobbit):
                arr.remove(i)
                arr.remove(j)
                break 
break를 쓰면 해당 반복문만 빠져나오고 다시 반복문이 돌기 떄문에 주의해야 한다. 
exit() - 프로그램 강제 종료
'''

for i in arr:
    for j in arr:
        if(i != j):
            if(i+j == hobbit):
                hobbitA = i
                hobbitB = j
arr.remove(hobbitA)
arr.remove(hobbitB)
arr.sort()
for i in arr:
    print(i, end='\n')
