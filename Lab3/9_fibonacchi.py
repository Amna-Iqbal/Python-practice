i = 0
j = 1
k = 0
print(i, end=",")
print(j, end=",")
for x in range(0, 51):
    k = i + j
    if k > 51:
        break

    print(k, end=",")
    i = j
    j = k