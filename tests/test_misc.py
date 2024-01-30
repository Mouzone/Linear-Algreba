import pytest
from linear_algebra.basic import Matrix, MatrixInitializationError

class TestMatrix:
    def test_flatten_non_empty_matrix(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        assert matrix.flatten() == [1, 2, 3, 4, 5, 6]

    def test_str_non_empty_matrix(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        expected_output = "1 2 3\n4 5 6"
        assert str(matrix) == expected_output
