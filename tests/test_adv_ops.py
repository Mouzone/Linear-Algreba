import pytest
from linear_algebra.matrix import Matrix

class TestTranspose:
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