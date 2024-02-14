class TestAppendMatrix:
    def test_sample_matrices():
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        return matrix1, matrix2

    def test_test_valid_append(sample_matrices):
        matrix1, matrix2 = sample_matrices
        result_matrix = matrix1.append(matrix2)
        expected_result = Matrix([[1, 2, 5, 6], [3, 4, 7, 8]])
        assert result_matrix.data == expected_result.data

    def test_matrix_vector():
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


class TestRearrange:

    def test_vector(self):
        vector = Matrix([1, 2, 3, 4])
        correct_vector = Matrix([4, 1, 2, 3])
        vector = Matrix.rearrange_rows(vector, 0)
        assert vector.container == correct_vector.container
    
    def test_matrix(self):
        matrix = Matrix([[7, 3, 8], [1, 9, 2], [6, 5, 4]])
        correct_matrix = Matrix([[7, 3, 8], [1, 9, 2], [6, 5, 4]])
        matrix = Matrix.rearrange_rows(matrix, 0)
        assert matrix.container == correct_matrix.container

    def test_height_greater_than_width(self):
        matrix = Matrix([[5, 2, 8], [1, 6, 3], [9, 4, 7], [2, 8, 1], [7, 3, 6], [4, 9, 5], [3, 1, 2], [6, 7, 4]])
        correct_matrix = Matrix([[9, 4, 7], [4, 9, 5], [5, 2, 8], [1, 6, 3], [2, 8, 1], [7, 3, 6], [3, 1, 2], [6, 7, 4]])
        matrix = Matrix.rearrange_rows(matrix, 0)
        assert matrix.container == correct_matrix.container

    def test_width_greater_than_height(self):
        matrix = Matrix([[4, 2, 7, 1, 9], [6, 3, 8, 5, 2], [1, 9, 4, 7, 3]])
        correct_matrix = Matrix([[6, 3, 8, 5, 2], [1, 9, 4, 7, 3], [4, 2, 7, 1, 9]])
        matrix = Matrix.rearrange_rows(matrix, 0)
        assert matrix.container == correct_matrix.container

    def test_duplicate_rows(self):
        matrix = Matrix([[6, 2, 7, 1, 9], [6, 3, 8, 5, 2], [4, 9, 4, 7, 3]])
        correct_matrix = Matrix([[6, 3, 8, 5, 2], [4, 9, 4, 7, 3], [6, 2, 7, 1, 9]])
        matrix = Matrix.rearrange_rows(matrix, 0)
        assert matrix.container == correct_matrix.container
    
    def test_negative_values(self):
        matrix = Matrix([[ 4, -2,  7, -1,  9], [-6,  3, -8,  5, -2], [ 1, -9,  4, -7,  3]])
        correct_matrix = Matrix([[-6,  3, -8,  5, -2], [ 1, -9,  4, -7,  3], [ 4, -2,  7, -1,  9]])
        matrix = Matrix.rearrange_rows(matrix, 0)
        assert matrix.container == correct_matrix.container

class TestReduce:

    @staticmethod
    def are_matrices_equal(matrix1, matrix2, tolerance=1e-9):
        return all(all(abs(val1 - val2) < tolerance for val1, val2 in zip(row1, row2)) for row1, row2 in zip(matrix1, matrix2))

    def test_reduce_row_1(self):
        matrix = Matrix([[7, 3, 8], [1, 9, 2], [6, 5, 4]])
        correct_matrix = Matrix([[1, 3/7, 8/7], [0, 9-3/7, 2-8/7], [0, 5-6*3/7, 4-6*8/7]])
        matrix = Matrix.rearrange_rows(matrix, 0)
        matrix = Matrix.reduce(matrix, 0)
        
        assert self.are_matrices_equal(matrix.container, correct_matrix.container, tolerance=0.01)

    def test_reduce_row_1(self):
        matrix =  Matrix([[1, 0, 0], [0, 5, 4], [0, 10, 47]])
        correct_matrix = Matrix([[1, 0, 0], [0, 1, 4.7], [0, 0, 4-5*4.7]])
        matrix = Matrix.rearrange_rows(matrix, 0)
        matrix = Matrix.reduce(matrix, 1)
        
        assert self.are_matrices_equal(matrix.container, correct_matrix.container, tolerance=0.01)
        
class TestGaussianElimination:
     def test_example_1(self):
        A = Matrix([[1, 2], [4, 9]])
        b = Matrix([5, 21])
        x = A.gaussian_elimination(b)
        answer = Matrix([3, 1])
        assert x.container == answer.container