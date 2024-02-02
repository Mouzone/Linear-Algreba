import pytest
from linear_algebra.basic import Matrix, MatrixInitializationError

class Solve_Requirements:
    def one_matrice(self):
        vector = Matrix([1, 2, 3, 4])

        with pytest.raises(MatrixInitializationError, match="Inputs must be Matrice"):
            vector_1.check_before_operations("dog")

        with pytest.raises(MatrixInitializationError, match="Heights are incompatible"):
            "dog".check_before_operations(vector)

class Rearrange:

    def test_vector(self):
        vector = Matrix([4, 3, 2, 1])
        correct_vector = Matrix([1, 2, 3, 4])
        assert(vector.container == correct_vector.container)
    
    def test_matrix(self):
        matrix = Matrix([[7, 3, 8], [1, 9, 2], [6, 5, 4]])
        correct_matrix = Matrix([[7, 3, 8], [1, 9, 2], [6, 5, 4]])
        assert(matrix.container == correct_matrix)

    def height_greater_than_width(self):
        matrix = Matrix([[5, 2, 8], [1, 6, 3], [9, 4, 7], [2, 8, 1], [7, 3, 6], [4, 9, 5], [3, 1, 2], [6, 7, 4]])
        correct_matrix = Matrix([[9, 4, 7], [4, 9, 5], [5, 2, 8], [1, 6, 3], [2, 8, 1], [7, 3, 6], [3, 1, 2], [6, 7, 4]])
        assert(matrix.container == correct_matrix)

    def width_greater_than_height(self):
        matrix = Matrix([[4, 2, 7, 1, 9], [6, 3, 8, 5, 2], [1, 9, 4, 7, 3]])
        correct_matrix = Matrix([[6, 3, 8, 5, 2], [1, 9, 4, 7, 3], [4, 2, 7, 1, 9]])
        assert(matrix.container == correct_matrix)

    def duplicate_rows(self):
        matrix = Matrix([[6, 2, 7, 1, 9], [6, 3, 8, 5, 2], [4, 9, 4, 7, 3]])
        correct_matrix = Matrix([[6, 3, 8, 5, 2], [4, 9, 4, 7, 3], [6, 2, 7, 1, 9]])
        assert(matrix.container == correct_matrix)
    
    def negative_values(self):
        matrix = Matrix([[ 4, -2,  7, -1,  9], [-6,  3, -8,  5, -2], [ 1, -9,  4, -7,  3]])
        correct_matrix = Matrix([[-6,  3, -8,  5, -2], [ 1, -9,  4, -7,  3], [ 4, -2,  7, -1,  9]])
        assert(matrix.container == correct_matrix)
