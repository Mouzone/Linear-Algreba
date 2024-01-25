import pytest
import re
from linear_algebra.basic_operations import Matrix, MatrixInitializationError

class TestMatrix:
    def test_empty_matrix_creation(self):
        matrix = Matrix()
        assert matrix.container == [[]]
        assert matrix.height == 0
        assert matrix.width == 0

    def test_single_element_matrix_creation(self):
        matrix = Matrix([[0]])
        assert matrix.container == [[0]]
        assert matrix.height == 1
        assert matrix.width == 1

    def test_valid_matrix_creation(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        assert matrix.container == [[1, 2, 3], [4, 5, 6]]
        assert matrix.height == 2
        assert matrix.width == 3

    def test_empty_matrix_creation_failure(self):
        with pytest.raises(MatrixInitializationError, match=re.escape("Input must be a non-empty list of lists")):
            matrix = Matrix([])

    def test_invalid_input_type_failure(self):
        with pytest.raises(MatrixInitializationError, match=re.escape("Input must be a non-empty list of lists")):
            matrix = Matrix("invalid_input")

    def test_invalid_input_row_not_list_failure(self):
        with pytest.raises(MatrixInitializationError, match=re.escape("Row 2 is not a list")):
            matrix = Matrix([[1, 2, 3], "invalid_row"])

    def test_invalid_input_row_length_mismatch_failure(self):
        with pytest.raises(MatrixInitializationError, match=re.escape("Row 2 has a different length than row 1")):
            matrix = Matrix([[1, 2, 3], [4, 5]])

    def test_invalid_input_element_not_int_failure(self):
        with pytest.raises(MatrixInitializationError, match=re.escape("Element at position (1, 2) is not an integer")):
            matrix = Matrix([[1, "invalid", 3], [4, 5, 6]])
