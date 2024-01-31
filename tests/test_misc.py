import pytest
from linear_algebra.basic import Matrix, MatrixInitializationError

class Flatten_Print:
    # flatten
    def test_flatten_non_empty_matrix(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        assert matrix.flatten() == [1, 2, 3, 4, 5, 6]

    # print
    def test_str_non_empty_matrix(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        expected_output = "1 2 3\n4 5 6"
        assert str(matrix) == expected_output

class IdentityMatrix:
    def identity_matrix_1x1(self):
        # dimension 1
        matrix = Matrix([[1]])
        assert identity_matrix(1).container == matrix.container

    def identity_matrix_3x3(self):
        # dimension 3
        matrix = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        assert identity_matrix(3).container == matrix.container

class AppendMatrix:
    def sample_matrices():
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        return matrix1, matrix2

    def test_valid_append(sample_matrices):
        matrix1, matrix2 = sample_matrices
        result_matrix = matrix1.append(matrix2)
        expected_result = Matrix([[1, 2, 5, 6], [3, 4, 7, 8]])
        assert result_matrix.data == expected_result.data

    def matrix_vector():
        matrix1 = Matrix([[1, 2], [4, 5]])
        matrix2 = Matrix([[3], [6]])
        return matrix1, matrix2

    def test_valid_append(sample_matrices):
        matrix1, matrix2 = sample_matrices
        result_matrix = matrix1.append(matrix2)
        expected_result = Matrix([[1, 2, 3], [4, 5, 6]])
        assert result_matrix.data == expected_result.data

    def test_incompatible_heights(sample_matrices):
        matrix1, matrix2 = sample_matrices
        matrix2.data = [[5, 6]]  # Change matrix2 to have incompatible heights
        with pytest.raises(MatrixInitializationError, match="Heights are incompatible"):
            matrix1.append(matrix2)

    def test_invalid_input_type():
        matrix = Matrix([[1, 2], [3, 4]])
        with pytest.raises(MatrixInitializationError, match="Inputs must be Matrices"):
            matrix.append([5, 6])
