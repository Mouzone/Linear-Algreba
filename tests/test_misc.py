import pytest
from linear_algebra.matrix import Matrix
from linear_algebra import utility

class TestFlatten_Print:
    # flatten
    def test_flatten_non_empty_matrix(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        assert matrix.flatten() == [1, 2, 3, 4, 5, 6]

    # print
    def test_str_non_empty_matrix(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        expected_output = "1 2 3\n4 5 6"
        assert str(matrix) == expected_output

class TestIdentityMatrix:
    def test_identity_matrix_1x1(self):
        # dimension 1
        matrix = Matrix([[1]])
        assert utility.identity_matrix(1).container == matrix.container

    def test_identity_matrix_3x3(self):
        # dimension 3
        matrix = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        assert utility.identity_matrix(3).container == matrix.container

