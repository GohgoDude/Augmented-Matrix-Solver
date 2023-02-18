# Augmented Matrix Solver

# Steps
# 1) Locate the leftmost nonzero column
# 2) Introduce leading 1 (divide row by x)
# 3) Interchange rows to introduce a nonzero number in the top left position
# 4) Clear below the 1 to introduce 0 (multiply rows placed underneath)
# 5) Ignoring the now completed first row, repeat Steps 1 to 4 for the remaining rows
# REF
# 6) Begin with the last nonzero row and working upward, clear above the leading 1 (work backwards)
# RREF

#code loop begins here
isOver = False
first_nonzero = [0][0]
# main_index = 0
matrix = []

row_count = int(input("Please input matrix rows (equations): "))
column_count = int(input("Please input matrix columns (variables + 1): "))

# Display
# print(str(row_count) + " rows\n" +
#       str(column_count) + " columns")
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
            i = 0
            print("First nonzero number found in row " + str(row) + ", column " + str(column))
            first_nonzero = matrix[row][column]
            # main_index = row
            # If anything breaks, change all (row) to (main_index)
            print("Nonzero number to divide row with: " + str(first_nonzero))
            print("Row of first nonzero: " + str(row))
            
# Step 2: Introduce leading 1 (divide row by x)
            matrix[row] = [x / first_nonzero for x in matrix[row]]
            matrix[i], matrix[row] = matrix[row], matrix[i]

            # Issue: struggling to figure out a way to ignore rows that have already been worked on
            # Potential solution: incrementing i

            i = i+1
            isOver = True
        if isOver:
            break
    if isOver:
        break

print()

for row in range(row_count):
    print(matrix[row])

# Future Issues:
# Even if inconsistency but presence of leading 1 in bn column, solve anyways
# If no more leading 1s possible to create but more columns exist to the right, find a way to ignore them and start working backwards
# Identity matrix analysis order:
#   check for inconsistent row (if none, continue)
#   check for free variable (missing leading 1 when compared to how many expected in row_count and column_count (if none, continue)
#   assign Xn to bn and state unique solution
