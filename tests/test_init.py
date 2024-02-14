import pytest
import re
from linear_algebra.matrix import matrix
class TestMatrix:

    def test_single_element_matrix_creation(self):
        matrix = Matrix([[0]])
        assert matrix.container == [[0]]
        assert matrix.height == 1
        assert matrix.width == 1

    def test_single_element_matrix_creation_second(self):
        matrix = Matrix([0])
        assert matrix.container == [[0]]
        assert matrix.height == 1
        assert matrix.width == 1

    def test_mixed_vector(self):
        with pytest.raises(MatrixInitializationError, match=re.escape("Matrix Initialization Error: Row 2 is not a list")):
            matrix = Matrix([[0], 0])
    
    def test_mixed_vector_2(self):
        with pytest.raises(MatrixInitializationError, match=re.escape("Matrix Initialization Error: Must be all integers")):
            matrix = Matrix([0, [0]])

    def test_valid_matrix_creation(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        assert matrix.container == [[1, 2, 3], [4, 5, 6]]
        assert matrix.height == 2
        assert matrix.width == 3

    def test_empty_matrix_creation(self):
        with pytest.raises(MatrixInitializationError, match=re.escape("Matrix Initialization Error: Matrix must be initialized with a non-empty list")):
            matrix = Matrix([[]])

    def test_empty_matrix_creation_failure(self):
        with pytest.raises(MatrixInitializationError, match=re.escape("Matrix Initialization Error: Matrix must be initialized with a non-empty list")):
            matrix = Matrix([])

    def test_invalid_input_type_failure(self):
        with pytest.raises(MatrixInitializationError, match=re.escape("Matrix Initialization Error: Matrix must be initialized with a non-empty list")):
            matrix = Matrix("invalid_input")

    def test_invalid_input_row_not_list_failure(self):
        with pytest.raises(MatrixInitializationError, match=re.escape("Matrix Initialization Error: Row 2 is not a list")):
            matrix = Matrix([[1, 2, 3], "invalid_row"])

    def test_invalid_input_row_length_mismatch_failure(self):
        with pytest.raises(MatrixInitializationError, match=re.escape("Matrix Initialization Error: Row 2 has a different length than row 1")):
            matrix = Matrix([[1, 2, 3], [4, 5]])

    def test_invalid_input_element_not_int_failure(self):
        with pytest.raises(MatrixInitializationError, match=re.escape("Matrix Initialization Error: Must be all integers")):
            matrix = Matrix([[1, "invalid", 3], [4, 5, 6]]) 
