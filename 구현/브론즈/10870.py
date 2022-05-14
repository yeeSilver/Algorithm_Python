'''
10870) 피보나치 수
'''

# --- 런타임 에러 : 왜 이거는 에러가 나는 거지 ?.?


def fibo(n):
    if(n-2 == 0) or (n-1 == 0):
        return 1
    return fibo(n-1)+fibo(n-2)


n = int(input())
print(fibo(n))
'''
fibo(5)
fibo(4)+fibo(3) = 2+2+1
fibo(4) = fibo(3)+fibo(2) = 2+1
fibo(3) = fibo(2)+fibo(1) = 2

'''

# ---에러없는 코드


def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1)+fibo(n-2)


n = int(input())
print(fibo(n))
'''
fibo(5)
fibo(4)+fibo(3) = 3+2
fibo(4) = fibo(3)+fibo(2) = 2+1
fibo(3) = fibo(2)+fibo(1) = 1+1
fibo(2) = fibo(1)+fibo(0) = 1
fibo(1) = 1 fibo(0) = 0
'''
