'''
16968)
'''

plate = input()
if plate[0] == 'c':
    result = 26
else:
    result = 10
print(result)

for i in range(1, len(plate)):
    if (plate[i-1] == plate[i]):
        if(plate == 'c'):
            result *= 25
            print(result)
        else:
            result *= 9
            print(result)
    else:
        if(plate == 'c'):
            result *= 26
            print(result)
        else:
            result *= 10
            print(result)
print(result)
