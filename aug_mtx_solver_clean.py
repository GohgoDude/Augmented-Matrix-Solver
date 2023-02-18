# Augmented Matrix Solver

isOver = False
first_nonzero = [0][0]
main_index = [0][0]
matrix = []

row_count = int(input("Please input matrix rows (equations): "))
column_count = int(input("Please input matrix columns (variables + 1): "))

print()

for row in range(row_count):
    equations = []
    for column in range(column_count):
        equations.append(float(input("(row " + str(row) + ", column " + str(column) + ") value: ")))
    matrix.append(equations)

for row in range(row_count):
    print(matrix[row])

print()

# Step 1: Locate the leftmost nonzero column (skip until found)

for column in range(column_count):
    for row in range(row_count):
        if matrix[row][column] != 0:
            first_nonzero = matrix[row][column]
            main_index = [row][column]
            matrix[main_index] = [x / first_nonzero for x in matrix[main_index]]
            matrix[0], matrix[main_index] = matrix[main_index], matrix[0]
            isOver = True
        if isOver:
            break
    if isOver:
        break

print()

for row in range(row_count):
    print(matrix[row])
