# program to add 2 matrices
def add_matrices(matrix1, matrix2):
    # check if the matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions")

    # create a result matrix with the same dimensions filled with zeros
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

    # add the corresponding elements of the two matrices
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result

print("Enter the dimensions of the matrices (rows and columns):")
rows = int(input("Rows: "))
cols = int(input("Columns: "))
print("Enter the first matrix:")
matrix1 = []
for i in range(rows):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    matrix1.append(row)
print("Enter the second matrix:")
matrix2 = []
for i in range(rows):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    matrix2.append(row)
try:
    result = add_matrices(matrix1, matrix2)
    print("Result of addition:")
    for row in result:
        print(row)
except ValueError as e:
    print(e)
