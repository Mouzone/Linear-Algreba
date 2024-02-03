import pytest
from linear_algebra.basic import Matrix, MatrixInitializationError

class TestSolve_Requirements:
    def test_one_matrice(self):
        vector = Matrix([1, 2, 3, 4])

        with pytest.raises(MatrixInitializationError, match="Target must be Matrix"):
            vector.solve("dog")
    
    def test_heights_not_equal(self):
        matrix_1 = Matrix([[5, 2, 8], [1, 6, 3], [9, 4, 7], [2, 8, 1], [7, 3, 6], [4, 9, 5], [3, 1, 2], [6, 7, 4]]) 
        matrix_2 = Matrix([[5, 2, 8], [1, 6, 3], [9, 4, 7], [2, 8, 1], [7, 3, 6], [4, 9, 5], [3, 1, 2]])

        with pytest.raises(MatrixInitializationError, match="Dimensions are incompatible"):
            matrix_1.solve(matrix_2)


class TestRearrange:

    def test_vector(self):
        vector = Matrix([1, 2, 3, 4])
        correct_vector = Matrix([4, 1, 2, 3])
        vector = Matrix.rearrange_rows(vector, vector.width)
        assert vector.container == correct_vector.container
    
    def test_matrix(self):
        matrix = Matrix([[7, 3, 8], [1, 9, 2], [6, 5, 4]])
        correct_matrix = Matrix([[7, 3, 8], [1, 9, 2], [6, 5, 4]])
        matrix = Matrix.rearrange_rows(matrix, matrix.width)
        assert matrix.container == correct_matrix.container

    def test_height_greater_than_width(self):
        matrix = Matrix([[5, 2, 8], [1, 6, 3], [9, 4, 7], [2, 8, 1], [7, 3, 6], [4, 9, 5], [3, 1, 2], [6, 7, 4]])
        correct_matrix = Matrix([[9, 4, 7], [4, 9, 5], [5, 2, 8], [1, 6, 3], [2, 8, 1], [7, 3, 6], [3, 1, 2], [6, 7, 4]])
        matrix = Matrix.rearrange_rows(matrix, matrix.width)
        assert matrix.container == correct_matrix.container

    def test_width_greater_than_height(self):
        matrix = Matrix([[4, 2, 7, 1, 9], [6, 3, 8, 5, 2], [1, 9, 4, 7, 3]])
        correct_matrix = Matrix([[6, 3, 8, 5, 2], [1, 9, 4, 7, 3], [4, 2, 7, 1, 9]])
        matrix = Matrix.rearrange_rows(matrix, matrix.width)
        assert matrix.container == correct_matrix.container

    def test_duplicate_rows(self):
        matrix = Matrix([[6, 2, 7, 1, 9], [6, 3, 8, 5, 2], [4, 9, 4, 7, 3]])
        correct_matrix = Matrix([[6, 3, 8, 5, 2], [4, 9, 4, 7, 3], [6, 2, 7, 1, 9]])
        matrix = Matrix.rearrange_rows(matrix, matrix.width)
        assert matrix.container == correct_matrix.container
    
    def test_negative_values(self):
        matrix = Matrix([[ 4, -2,  7, -1,  9], [-6,  3, -8,  5, -2], [ 1, -9,  4, -7,  3]])
        correct_matrix = Matrix([[-6,  3, -8,  5, -2], [ 1, -9,  4, -7,  3], [ 4, -2,  7, -1,  9]])
        matrix = Matrix.rearrange_rows(matrix, matrix.width)
        assert matrix.container == correct_matrix.container

class TestReduce:

    def test_reduce(self):
        matrix = Matrix([[7, 3, 8], [1, 9, 2], [6, 5, 4]])
        correct_matrix = Matrix([[1, 3/7, 8/7], [0, 9-3/7, 2-8/7], [0, 5-6*3/7, 4-6*8/7]])
        matrix = Matrix.rearrange_rows(matrix, matrix.width)
        matrix = reduce(matrix, 0)
        assert matrix.container == correct_matrix.container
        