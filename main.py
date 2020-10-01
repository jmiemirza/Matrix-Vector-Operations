from matrix import MatrixClass
from vector import VectorClass

if __name__ == "__main__":
    a = MatrixClass(2,2)
    b = MatrixClass(2,2)

    matrix_a = a.populate_matrix()
    matrix_b = b.populate_matrix()

    a.print_matrix(matrix_a)
    b.print_matrix(matrix_b)

    a.matrix_addition(matrix_a, matrix_b)

    a.matrix_multiplication(matrix_a, matrix_b)