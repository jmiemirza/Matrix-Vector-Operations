class MatrixClass:
    ' ' ' A class for Matrix Multiplication' ' '

    def __init__(self, n, m):

        self.rows = n  # Number of rows
        self.cols = m  # Number of columns

    def populate_matrix(self):

        print("Please enter the values for the Matrix: ")
        matrix = [[int(input()) for i in range(self.cols)] for j in range(self.rows)]

        return matrix

    def print_matrix(self, matrix):

        print("The Matrix you have entered is: ")

        for i in range(self.rows):
            for j in range(self.cols):
                print(format(matrix[i][j], "<3"), end=" ")
            print()

    def matrix_addition(self, matrix_a, matrix_b):

        result = [[0 for i in range(self.cols)] for j in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = matrix_a[i][j] + matrix_b[i][j]

        print("ADDITION RESULT IS: ")
        for i in range(self.rows):
            for j in range(self.cols):
                print(format(result[i][j], "<3"), end=" ")
            print()

    def matrix_multiplication(self, matrix_a, matrix_b):

        n = self.rows

        result = [[0 for i in range(self.cols)] for j in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                for k in range(n):
                    result[i][j] = result[i][j] + matrix_a[i][k] * matrix_b[k][j]

        print("MULTIPLICATION RESULT IS: ")
        for i in range(self.rows):
            for j in range(self.cols):
                print(format(result[i][j], "<3"), end=" ")
        print()