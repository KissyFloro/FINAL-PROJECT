import numpy as np

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print()
print("Matrix:")
print(matrix)
print()
row_sums = matrix.sum(axis=1)
column_sums = matrix.sum(axis=0)

print("Row Sums:")
print (row_sums)
print()
print("Column Sums:")
print(column_sums)
print()


print(np.hstack((matrix, row_sums[:, None])))
print(column_sums)

