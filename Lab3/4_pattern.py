rows = 5
columns = 5
for i in range(rows):
    # nested loop
    for j in range(i):
        print("*", end=' ')
    print('')

rows = 5
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print("*", end=' ')
    print('\r')