rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
matrix = []

matrix = []
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(i * j)
    matrix.append(row)
print()
for row in matrix:
    print(row)
