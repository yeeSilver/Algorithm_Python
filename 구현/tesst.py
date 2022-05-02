c_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
str = input()
for word in c_alpha:
  str.replace(word,'*')
print(str)
