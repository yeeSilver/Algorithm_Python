arr = []
result = []
for i in range(9):
    arr.append(int(input()))

hobbit = sum(arr) - 100

for i in arr:
    for j in arr:
        if(i != j):
            if(i+j == hobbit):
                arr.remove(i)
                arr.remove(j)
                break
arr.sort()
for i in arr:
    print(i,end='\n')
