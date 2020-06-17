class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.elements = [[int(element) for element in input().split()] for row in range(self.rows)]

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
            print("ERROR")
            return None





m, n = map(int, input().split())  # Expected user input #1 is matrix dimensions m rows, n columns
#  Problem statement recommends using n for rows, and m for columns
#  but this is not standard matrix notation
matrix_A = Matrix(m, n)


i, j = map(int, input().split())
matrix_B = Matrix(i, j)

result = matrix_A + matrix_B
if result:
    for row in result:
        print(*row)
