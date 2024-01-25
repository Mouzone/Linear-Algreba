import pytest
from linear_algebra.basic import Matrix, MatrixInitializationError

class TestMatrixOperations:
    def test_check_before_operations_same_dimensions(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        # Should not raise any exceptions
        matrix1.check_before_operations(matrix2)

    def test_check_before_operations_different_heights(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6]])
        with pytest.raises(MatrixInitializationError, match="Heights are incompatible"):
            matrix1.check_before_operations(matrix2)

    def test_check_before_operations_different_widths(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6, 7], [8, 9, 10]])
        with pytest.raises(MatrixInitializationError, match="Widths are incompatible"):
            matrix1.check_before_operations(matrix2)

    def test_matrix_addition(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        result = matrix1 + matrix2
        assert result.container == [[6, 8], [10, 12]]

    def test_matrix_subtraction(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        result = matrix1 - matrix2
        assert result.container == [[-4, -4], [-4, -4]]

    def test_matrix_addition_incompatible_dimensions(self):
        matrix1 = Matrix([[1, 2], [3, 4], [5, 6]])
        matrix2 = Matrix([[5, 6,], [8, 9]])
        with pytest.raises(MatrixInitializationError, match="Heights are incompatible"):
            result = matrix1 + matrix2

    def test_matrix_subtraction_incompatible_dimensions(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6, 7], [8, 9, 10]])
        with pytest.raises(MatrixInitializationError, match="Widths are incompatible"):
            result = matrix1 - matrix2
