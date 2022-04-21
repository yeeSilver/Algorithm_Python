result = []
array = []

    
def solution(n):
    answer = 0
    while n > 0:
        answer += n % 10
        n //= 10  # n=n//10(n을 10으로 나눈 뒤 몫의 정수만 다시 가져와)
    return answer


    
for i in range(1, 10000):
    num = solution(i) + i
    print('i = %d, num = %d'%(i, num))
    if (num<= 10000) :
        result.append(num)
    
for j in range(1, 10000):
    if j not in result:
        array.append(j)

print(array)
