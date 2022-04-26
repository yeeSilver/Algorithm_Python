'''
5622) 다이얼 문제

'''
alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
dic = {}
# 왜 안됨??
# for i in range(1, 15, 3):
#   dict[i] = [alphabet[i], alphabet[i+1], alphabet[i+2]]
# print(dic)
dic = {3: ["a", 'b'], 2: ['c', 'n']}
dic[1] = [alphabet[1], 'bls']
print(dic[1])
