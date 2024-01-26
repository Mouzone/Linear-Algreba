import pytest
from linear_algebra.basic import Matrix, MatrixInitializationError

class TestMatrixOperations:
    def test_transpose_square_matrix(self):
        matrix_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix = Matrix(matrix_data)
        transposed_matrix = matrix.transpose()

        expected_result = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        assert transposed_matrix.container == expected_result

    def test_transpose_rectangular_matrix(self):
        matrix_data = [[1, 2, 3], [4, 5, 6]]
        matrix = Matrix(matrix_data)
        transposed_matrix = matrix.transpose()

        expected_result = [[1, 4], [2, 5], [3, 6]]
        assert transposed_matrix.container == expected_result

    def test_transpose_empty_matrix(self):
        matrix_data = [[]]
        matrix = Matrix(matrix_data)
        transposed_matrix = matrix.transpose()

        # Transposing an empty matrix should still result in an empty matrix
        assert transposed_matrix.container == [[]]