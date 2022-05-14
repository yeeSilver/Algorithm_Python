
'''num = int(input())

arrList = []
for i in range(num):
    arrList.append(list(map(int, input().split())))


def grade(arr):
    grade = 1
    result = []
    arr.sort(reverse=True)
    for i in range(len(arr)-1):
        if(arr[i][1] > arr[i+1][1]):
            result.append(grade)
            grade = i+2
        else:
            result.append(grade)
    result.append(len(arr))
    return result


result = grade(arrList)
for i in result:
    print(i, end=' ')
'''
arr = [[1,2],[3,4], [5, 6]]
for i in arr:
    for j in arr:
        print(i[0], j[0])
