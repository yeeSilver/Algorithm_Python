'''
10951) 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오

무한반복
1) while True :
   try:
     (code)
    except: try에 에러가 발생할 시 예외처리
      break
    
2) for문으로 무한반복하는 건 아직 못 봄.. 

* 주의! 예외처리까지 해줘야 코드 정상적으로 실행됨
'''
# --- 런타임 에러 코드 ---
# 주의! 예외처리까지 해줘야 코드 정상적으로 실행됨
# while True:
#     arr = list(map(int, input().split()))
#     print(arr[0] + arr[1])

# === 정상 작동 코드 ---
while True:
    try:
        arr = list(map(int, input().split()))
        print(arr[0] + arr[1])
    except:
        break
