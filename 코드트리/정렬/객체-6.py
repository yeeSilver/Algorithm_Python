# 이름, 번지수, 지역에 대한 n명의 자료가 주어지면, 사전순으로 이름이 가장 느린 사람의 자료를 출력하는 프로그램을 작성해보세요
class Address:
    def __init__(self, name, call, city):
        self.name = name
        self.call = call
        self.city = city


n = int(input())
arr = [tuple(input().split()) for _ in range(n)]


# 변수를 객체에 넣어 저장

people = [
    Address(name, call, city)
    for name, call, city in arr
]

# 사전순 이름 느린사람
dic_idx = 0


for i in range(n):
    if people[dic_idx].name < people[i].name:
        dic_idx = i
print(f"name {people[dic_idx].name}")
print(f"addr {people[dic_idx].call}")
print(f"city {people[dic_idx].city}")
