import pytest
from linear_algebra.matrix import Matrix, MatrixInitializationError
from linear_algebra.solve.gaus_elim import *

class TestCheck_Upper_Triangular:

    def test_has_upper_elements(self):
        matrix1 = Matrix([[1, 0.2, 0.3, 0.4], [0, 1, 0.5, 0.6], [0, 0, 1, 0.7]])
        matrix2 = Matrix([0, 0, 0])
        matrix = Aug_matrix(matrix1, matrix2)
        assert check_upper_triangular(matrix) == False

    def test_pivot_is_not_1(self):
        matrix1 = Matrix([[1, 0.2, 0.3, 0.4], [0, 1, 0.5, 0.6], [0, 0, 1, 0.7], [0, 0, 0, 5]])
        matrix2 = Matrix([0, 0, 0, 0])
        matrix = Aug_matrix(matrix1, matrix2)
        assert check_upper_triangular(matrix) == False

    def test_lower_has_elements(self):
        matrix1 = Matrix([[1, 0.2, 0.3, 0.4], [1, 1, 0.5, 0.6], [0, 0, 1, 0.7], [3, 4, 0, 1]])
        matrix2 = Matrix([0, 0, 0, 0])
        matrix = Aug_matrix(matrix1, matrix2)
        assert check_upper_triangular(matrix) == False

# test append and check_inputs
class TestAppendMatrix:
    @pytest.fixture
    def sample_matrices(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        return matrix1, matrix2

    def test_valid_append(self, sample_matrices):
        matrix1, matrix2 = sample_matrices
        result_matrix = Aug_matrix(matrix1, matrix2)
        expected_result = Matrix([[1, 2, 5, 6], [3, 4, 7, 8]])
        assert result_matrix.container == expected_result.container

    @pytest.fixture
    def matrix_vector(self):
        matrix1 = Matrix([[1, 2], [4, 5]])
        matrix2 = Matrix([3, 6])
        return matrix1, matrix2

    def test_valid_append_matrix_vector(self, matrix_vector):
        matrix1, matrix2 = matrix_vector
        result_matrix = Aug_matrix(matrix1, matrix2)
        expected_result = Matrix([[1, 2, 3], [4, 5, 6]])
        assert result_matrix.container == expected_result.container

    def test_incompatible_heights(self, matrix_vector):
        matrix1, matrix2 = matrix_vector
        matrix2 = Matrix([5])  # Change matrix2 to have incompatible heights
        with pytest.raises(MatrixInitializationError, match="Dimensions are not compatible"):
            Aug_matrix(matrix1, matrix2)


class TestRearrange:

    def test_vector(self):
        matrix1 = Matrix([1,2,3,4])
        matrix2 = Matrix([0,0,0,0])
        vector = Aug_matrix(matrix1, matrix2)
        correct_vector = Matrix([[4,0],[1,0], [2,0], [3,0]])
        vector = rearrange_rows(vector, 0)
        assert vector == correct_vector.container
    
    def test_matrix(self):
        matrix1 = Matrix([[7, 3], [1, 9], [6, 5]])
        matrix2 = Matrix([8,2,4])
        matrix = Aug_matrix(matrix1, matrix2)
        correct_matrix = Matrix([[7, 3, 8], [1, 9, 2], [6, 5, 4]])
        matrix = rearrange_rows(matrix, 0)
        assert matrix == correct_matrix.container

    def test_height_greater_than_width(self):
        matrix1 =  Matrix([[5, 2], [1, 6], [9, 4], [2, 8], [7, 3], [4, 9], [3, 1], [6, 7]])
        matrix2 = Matrix([8, 3, 7, 1, 6, 5, 2, 4])
        matrix = Aug_matrix(matrix1, matrix2)
        correct_matrix = Matrix([[9, 4, 7], [4, 9, 5], [5, 2, 8], [1, 6, 3], [2, 8, 1], [7, 3, 6], [3, 1, 2], [6, 7, 4]])
        matrix = rearrange_rows(matrix, 0)
        assert matrix == correct_matrix.container

    def test_width_greater_than_height(self):
        matrix1 = Matrix([[4, 2, 7, 1], [6, 3, 8, 5], [1, 9, 4, 7]])
        matrix2 = Matrix([9, 2, 3])
        matrix = Aug_matrix(matrix1, matrix2)
        correct_matrix = Matrix([[6, 3, 8, 5, 2], [1, 9, 4, 7, 3], [4, 2, 7, 1, 9]])
        matrix = rearrange_rows(matrix, 0)
        assert matrix == correct_matrix.container

    def test_duplicate_rows(self):
        matrix1 = Matrix([[6, 2, 7, 1], [6, 3, 8, 5], [4, 9, 4, 7]])
        matrix2 = Matrix([9, 2, 3])
        matrix = Aug_matrix(matrix1, matrix2)
        correct_matrix = Matrix([[6, 3, 8, 5, 2], [4, 9, 4, 7, 3], [6, 2, 7, 1, 9]])
        matrix = rearrange_rows(matrix, 0)
        assert matrix == correct_matrix.container
    
    def test_negative_values(self):
        matrix1 = Matrix([[ 4, -2,  7, -1], [-6,  3, -8,  5], [ 1, -9,  4, -7]])
        matrix2 = Matrix([9,-2,3])
        matrix = Aug_matrix(matrix1, matrix2)
        correct_matrix = Matrix([[-6,  3, -8,  5, -2], [ 1, -9,  4, -7,  3], [ 4, -2,  7, -1,  9]])
        matrix = rearrange_rows(matrix, 0)
        assert matrix == correct_matrix.container

class TestReduce:

    @staticmethod
    def are_matrices_equal(matrix1, matrix2, tolerance=1e-9):
        return all(all(abs(val1 - val2) < tolerance for val1, val2 in zip(row1, row2)) for row1, row2 in zip(matrix1, matrix2))

    def test_reduce_row_1(self):
        matrix1 = Matrix([[7, 3], [1, 9], [6, 5]])
        matrix2 = Matrix([8,2,4])
        matrix = Aug_matrix(matrix1, matrix2)
        correct_matrix = Matrix([[1, 3/7, 8/7], [0, 9-3/7, 2-8/7], [0, 5-6*3/7, 4-6*8/7]])
        matrix.container = rearrange_rows(matrix, 0)
        matrix.container = reduce(matrix, 0)
        
        assert self.are_matrices_equal(matrix.container, correct_matrix.container, tolerance=0.01)

    def test_reduce_row_2(self):
        matrix1 =  Matrix([[1, 0], [0, 5], [0, 10]])
        matrix2 = Matrix([0,4,47])
        matrix = Aug_matrix(matrix1, matrix2)
        correct_matrix = Matrix([[1, 0, 0], [0, 1, 4.7], [0, 0, 4-5*4.7]])
        matrix.container = rearrange_rows(matrix, 0)
        matrix.container = reduce(matrix, 1)
        
        assert self.are_matrices_equal(matrix.container, correct_matrix.container, tolerance=0.01)
        
class TestGaussianElimination:
     def test_example_1(self):
        A = Matrix([[1, 2], [4, 9]])
        b = Matrix([5, 21])
        x = Aug_matrix(A,b)
        x.gaussian_elimination()
        answer = Matrix([3.0, 1.0])
        assert x.solution == answer.container