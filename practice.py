values = [2,-5,-2,-4,3]

max = -99999
n = 1

for val in values:
    n *= val

    if max < n:
        max = n
    
    if val == 0:
        n = 1

dummyMax = n
tmp = dummyMax

if len(values) > 1 and dummyMax < 0:
    for val in values:
        if val == 0:
            tmp = dummyMax
            continue

        tmp = tmp / val

        if max < tmp:
            max = tmp

print(max)

    

