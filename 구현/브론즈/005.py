'''
1008번) 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.
입력) 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
출력) 첫째 줄에 A/B를 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-9 이하이면 정답이다.

파이썬은 소수를 반복되기 전까지는 전부, 반복된다면 반복되는 부분을 추가로 16자리까지 출력하므로 오차범위를 생각할 필요가 없다. 라고 하는데... 왜지?

'''

a, b = map(int, input().split())
division = a/b
print(division)
