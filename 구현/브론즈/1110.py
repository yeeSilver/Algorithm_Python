'''
브론즈1) https://www.acmicpc.net/problem/1110

'''
num = int(input())


def newNum(num):
    numList = []
    if num < 10:
        numList.insert(0, 0)
        numList.insert(1, num)
    else:
        numList.insert(0, (num//10))
        numList.insert(1, (num % 10))
    print('numList', numList)
    addNum = numList[0]+numList[1]
    if addNum < 10:
        newNum = numList[1]*10 + addNum
    else:
        newNum = numList[1]*10 + (addNum % 10)

    return newNum


'''
num이랑 newNum이랑 같아질 때까지 함수 newNum(num)을 하도록 한다 
'''
newNumber = newNum(num)  # newNumber:50
count = 1  # count = 1
while (num != newNumber):  # num == newNumber가 되면 조건을 빠져나오겠지
    count += 1
    newNumber = newNum(newNumber)  # newNumber = newNum(50)
    print('new', newNumber)

print(count)
