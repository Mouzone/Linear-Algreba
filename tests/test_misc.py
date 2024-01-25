import pytest
from linear_algebra.basic_operations import Matrix, MatrixInitializationError

class TestMatrix:
    def test_flatten_empty_matrix(self):
        matrix = Matrix([[]])
        assert matrix.flatten() == []

    def test_flatten_non_empty_matrix(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        assert matrix.flatten() == [1, 2, 3, 4, 5, 6]

    def test_str_empty_matrix(self):
        matrix = Matrix([[]])
        expected_output = ""
        assert str(matrix) == expected_output

    def test_str_non_empty_matrix(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        expected_output = "1 2 3\n4 5 6"
        assert str(matrix) == expected_output
