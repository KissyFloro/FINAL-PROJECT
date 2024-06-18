def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range (len(matrix))] for i in range (len(matrix[0]))]

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("Input:")
for row in matrix:
    print(row)

output_matrix = transpose_matrix(matrix)
print("Output:")
for row in output_matrix:
    print(row)