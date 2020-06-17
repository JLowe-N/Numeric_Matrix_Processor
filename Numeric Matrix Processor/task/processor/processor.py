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
                    row.append(self.elements[m][n] * constant)
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


# Main Program
while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
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
        rows, columns, matrix_input = take_matrix_input("Enter size of first matrix: ", "Enter first matrix:")
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

    if choice == '0':
        break





