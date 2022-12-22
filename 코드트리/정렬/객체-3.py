class Code:
    def __init__(self, cname, score):
        self.cname = cname
        self.score = score


codes = []
for i in range(5):
    name, score = (input().split())
    score = int(score)
    codes.append(Code(name, score))

minScore = codes[0].score
minName = codes[0].cname

for i in range(1, 5):

    if codes[i].score < minScore:
        minScore = codes[i].score
        minName = codes[i].cname


print(f"{minName} {minScore}")
