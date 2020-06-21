import copy


class Matrix:
    def __init__(self, rows, columns, array):
        self.rows = rows
        self.columns = columns
        self.elements = array

    def create_row(self):
        return self.elements.append([int(element) for element in input().split()])

#    def __str__(self):
#        print('[')
#        for index, element in enumerate(self.elements):
#            print(self.elements[index], ',', sep='')
#        print(']')

    def __add__(self, other):
        if not isinstance(other, Matrix):
            print("ERROR")
            return None
        if self.rows == other.rows and self.columns == other.columns:
            matrix = []
            for m in range(self.rows):
                if m > 0:
                    matrix.append(row)
                row = []
                for n in range(self.columns):
                    row.append(self.elements[m][n] + other.elements[m][n])
            matrix.append(row)
            return matrix
        else:
            print("The operation cannot be performed")
            return None

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            matrix = []
            for m in range(self.rows):
                row = []
                for n in range(self.columns):
                    row.append(self.elements[m][n] * other)
                matrix.append(row)
            return matrix
        if isinstance(other, Matrix):
            matrix = []
            for m in range(self.rows):
                if m > 0:
                    matrix.append(row)
                row = []
                for j in range(other.columns):
                    element_sum = []
                    for n in range(self.columns):
                        element_sum.append(self.elements[m][n] * other.elements[n][j])
            #            print("n", f"{n+1}",element_sum)
            #        print(f"Sum of element-wise multiplication:", sum(element_sum))
                    row.append(sum(element_sum))
            #        print(f"Appending element {j+1} of row {m+1}: {row}")
            matrix.append(row)
            #print(f"Appending row {m+1} of matrix: {matrix}")
            return matrix
        else:
            print("ERROR")
            return None

    def transpose(self, type):
        #main diagonal
        if type == "main_diagonal":
            matrix = [[] for row in range(self.rows)]
            for m in range(self.rows):
                for n in range(self.columns):
                    matrix[self.rows-1-n].append(self.elements[m].pop())
            return matrix
        #side diagonal
        if type == "side_diagonal":
            matrix = [[] for row in range(self.rows)]
            for m in range(self.rows):
                for n in range(self.columns):
                    matrix[n].insert(0, self.elements[m].pop()) #pop right-left, append-left when starting new column
            return matrix
        #horizontal
        if type == "horizontal":
            matrix = []
            for _ in range(self.rows):
                matrix.append(self.elements.pop())
            return matrix
        #vertical
        if type == "vertical":
            matrix = []
            for i in range(self.rows):
                row = []
                for _ in range(self.columns):
                    row.append(self.elements[i].pop())
                matrix.append(row)
            return matrix


#matrix_test_1 = Matrix(2,3,[[1,0,17],[15,9,7]])
#matrix_test_2 = Matrix(3,4,[[5,6,78,9],[29,31,47,1],[14,17,0,3]])
#print(matrix_test_1 * matrix_test_2)

def convert_string_to_number(element):
    try:  # Check for integer
        a = float(element)
        b = int(a)
        if a == b:
            return b
    # If not integer, check for float
        else:
            return a
    except ValueError:
        print(f"Element {element} is not a number")
        return None


def take_matrix_input(input_prompt_1, input_prompt_2):
    rows, columns = map(int, input(f"{input_prompt_1}").split())
    print(f"{input_prompt_2}")
    matrix_input = [[convert_string_to_number(element) for element in input().split()] for row in range(rows)]
    return rows, columns, matrix_input


def create_matrix_object(rows, columns, matrix):
    if len(matrix) != rows:
        print("Invalid matrix dimensions")
        return None
    for row in matrix:
        if len(row) != columns:
            print("Invalid matrix dimensions")
            return None
        for element in row:
            if not isinstance(element, (int, float)):
                print(f"Invalid element type {type(element)} supplied")
                return None
    return Matrix(rows, columns, matrix)


def determinant(matrix):
    if isinstance(matrix, Matrix):
        matrix = matrix.elements
    rows = len(matrix)
    columns_set = set(len(row) for row in matrix)
    if len(columns_set) > 1:
        print("Column count is not consistent across rows")
        return None
    else:
        columns = columns_set.pop()
    if len(matrix) == 1:  # Edge-case
        return matrix[0][0]
    if len(matrix) == 2:  # Base-case
        base_case = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        #print(f"Base case: Determinant is {base_case} for {matrix}")
        return base_case
    else:
        determinants = []
        for n in range(columns):  # Will make a smaller matrix for each column by dropping elements of a copy
            #print(f"Recursing on row 0 and column {n} of matrix {matrix}")
            # Make a deepcopy so nested lists are not edited in original when dropping elements
            smaller_matrix = copy.deepcopy(matrix)
            del smaller_matrix[0]  # Drop the row we are working through for Laplace Expansion
            for row in smaller_matrix:
                del row[n]  # Drop the column we are working through for Laplace Expansion
            #print(f"Passing smaller matrix {smaller_matrix} back to function through recursion")
            determinants.append(matrix[0][n] * (-1) ** (n) * determinant(smaller_matrix))
        #print(f"Final determinant list {determinants}")
        return sum(determinants)

def find_cofactors(matrix):
    if isinstance(matrix, Matrix):
        matrix = matrix.elements
    rows = len(matrix)
    columns_set = set(len(row) for row in matrix)
    if len(columns_set) > 1:
        print("Column count is not consistent across rows")
        return None
    else:
        columns = columns_set.pop()
    if len(matrix) == 1:  # Edge-case
        return matrix[0][0]
    if len(matrix) == 2:  # Base-case
        base_case = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        #print(f"Base case: Determinant is {base_case} for {matrix}")
        return base_case
    else:
        cofactor_matrix = [[] for _ in range(rows)]
        for m in range(rows):
            for n in range(columns):  # Will make a smaller matrix for each column by dropping elements of a copy
                #print(f"Recursing on row {m} and column {n} results so far {cofactor_matrix}")
                # Make a deepcopy so nested lists are not edited in original when dropping elements
                smaller_matrix = copy.deepcopy(matrix)
                for row in smaller_matrix:
                    del row[n]  # Drop the column we are working through for Laplace Expansion
                del smaller_matrix[m]  # Drop the row we are working through for Laplace Expansion
                #print(f"row {m} and column {n} smaller matrix {smaller_matrix}")
                #print(f"Coefficient: {matrix[m][n]}, sign {(-1) ** ((m + 1) + (n + 1))}")
                cofactor_matrix[m].append((-1) ** ((m + 1) + (n + 1)) * determinant(smaller_matrix))
        return cofactor_matrix



# Main Program
while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    choice = input('Your choice: ')

    if choice == '1':
        rows, columns, matrix_input = take_matrix_input("Enter size of first matrix: ", "Enter first matrix:")
        matrix_A = create_matrix_object(rows, columns, matrix_input)
        rows, columns, matrix_input = take_matrix_input("Enter size of second matrix: ", "Enter second matrix:")
        matrix_B = create_matrix_object(rows, columns, matrix_input)
        result = matrix_A + matrix_B
        if result:
            print("The result is:")
            for row in result:
                print(*row)

    if choice == '2':
        rows, columns, matrix_input = take_matrix_input("Enter matrix size: ", "Enter matrix:")
        matrix_A = create_matrix_object(rows, columns, matrix_input)
        constant = convert_string_to_number(input("Enter constant: "))
        result = matrix_A * constant
        print("The result is:")
        if result:
            print("The result is:")
            for row in result:
                print(*row)

    if choice == '3':
        rows, columns, matrix_input = take_matrix_input("Enter size of first matrix: ", "Enter first matrix:")
        matrix_A = create_matrix_object(rows, columns, matrix_input)
        rows, columns, matrix_input = take_matrix_input("Enter size of second matrix: ", "Enter second matrix:")
        matrix_B = create_matrix_object(rows, columns, matrix_input)
        result = matrix_A * matrix_B
        if result:
            print("The result is:")
            for row in result:
                print(*row)

    if choice == '4':
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")
        subchoice_dict = {'1': 'main_diagonal', '2': 'side_diagonal', '3': 'vertical', '4': 'horizontal'}
        while True:
            subchoice = input()
            if subchoice not in subchoice_dict.keys():
                pass
            else:
                transpose_type = subchoice_dict[subchoice]
                rows, columns, matrix_input = take_matrix_input("Enter matrix size: ", "Enter matrix:")
                matrix_A = create_matrix_object(rows, columns, matrix_input)
                result = matrix_A.transpose(transpose_type)
                if result:
                    print("The result is:")
                    for row in result:
                        print(*row)
                break

    if choice == '5':
        rows, columns, matrix_input = take_matrix_input("Enter matrix size: ", "Enter matrix:")
        matrix_A = create_matrix_object(rows, columns, matrix_input)
        result = determinant(matrix_A)
        if result:
            print("The result is:")
            print(result)

    if choice == '6':
        rows, columns, matrix_input = take_matrix_input("Enter matrix size: ", "Enter matrix:")
        matrix_A = create_matrix_object(rows, columns, matrix_input)
        det_A = determinant(matrix_A)
        #print(det_A)
        if det_A != 0:
            cofactor_matrix = find_cofactors(matrix_A)
            #print(cofactor_matrix)
            cofactor_transpose = Matrix(rows, columns, Matrix(rows, columns, cofactor_matrix).transpose("main_diagonal"))
            #print(type(cofactor_transpose))
            #print(cofactor_transpose)
            result = cofactor_transpose * (1 / det_A) # cofactor inverse
            if result:
                print("The result is:")
                if result:
                    for row in result:
                        print(*row)
        else:
            print("This matrix doesn't have an inverse.")

    if choice == '0':
        break





