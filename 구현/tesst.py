def groupNum(arr):
    result = []
    result.append(arr[0])
    result.append(arr[1])
    for i in range(2, len(arr)):
        print(i)
        if arr[i] in result:
            if arr[i-1] == arr[i]:
                result.append(arr[i])
            else:
                pass
        else:
            result.append(arr[i])
    print((arr))
    print((result))

    if len(arr) == len(result):
        r = True
    else:
        r = False
    return r

arr = ['a', 'a', 'b']
print(groupNum(arr))

for i in range(1,3):
    print('프린트 %d' %(i))
