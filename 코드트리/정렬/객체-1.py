class Code:
    def __init__(self, secretCode, location, time):
        self.secretCode = secretCode
        self.location = location
        self.time = time


arr = list((input().split()))
code1 = Code(arr[0], arr[1], arr[2])

print(f"secret code : {code1.secretCode}")
print(f"meeting point : {code1.location}")
print(f"time : {code1.time}")
