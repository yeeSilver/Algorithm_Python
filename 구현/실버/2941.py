'''
2941) 크로아티아 알파벳 https://www.acmicpc.net/problem/2941
replace
- 문자열에서만 가능
- str.replace(old, new, count) *default는 count =1
ex)
  print('apple'.replace('p','k',1)) //akple
  print('apple'.replace('p','k',2)) //akkle

'''
# c_alpha = {'č': 'c=', 'ć': 'c-', 'dž': 'dz=', 'đ': 'd-',
#            'lj': 'lj', 'nj': 'nj', 'š': 's=', 'ž': 'z='}
c_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
input = input()
for word in c_alpha:
    input = input.replace(word, '*')
print(len(input))
