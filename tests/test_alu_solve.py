import pytest
from linear_algebra.basic import Matrix, MatrixInitializationError

class TestSolve_Requirements:
    def test_one_matrice(self):
        vector = Matrix([1, 2, 3, 4])

        with pytest.raises(MatrixInitializationError, match="Target must be Matrix"):
            vector.alu_solve("dog")
    
    def test_heights_not_equal(self):
        matrix_1 = Matrix([[5, 2, 8], [1, 6, 3], [9, 4, 7], [2, 8, 1], [7, 3, 6], [4, 9, 5], [3, 1, 2], [6, 7, 4]]) 
        matrix_2 = Matrix([[5, 2, 8], [1, 6, 3], [9, 4, 7], [2, 8, 1], [7, 3, 6], [4, 9, 5], [3, 1, 2]])

        with pytest.raises(MatrixInitializationError, match="Dimensions are incompatible"):
            matrix_1.alu_solve(matrix_2)

class TestCheck_Finished:

    def test_has_upper_elements(self):
        matrix = Matrix([[1, 0.2, 0.3, 0.4], [0, 1, 0.5, 0.6], [0, 0, 1, 0.7], [0, 0, 0, 1]])
        assert Matrix.check_finished(matrix, matrix.width) == True

    def test_pivot_is_not_1(self):
        matrix = Matrix([[1, 0.2, 0.3, 0.4], [0, 1, 0.5, 0.6], [0, 0, 1, 0.7], [0, 0, 0, 5]])
        assert Matrix.check_finished(matrix, matrix.width) == False

    def lower_has_elements(self):
        matrix = Matrix([[1, 0.2, 0.3, 0.4], [1, 1, 0.5, 0.6], [0, 0, 1, 0.7], [3, 4, 0, 1]])
        assert Matrix.check_finished(matrix, matrix.width) == False

class TestFactorization:

    def test_identity_matrix(self):
        matrix = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        L, U = matrix.alu_factorization()
        correct = Matrix.identity_matrix(3)
        assert L.container == correct.container
        assert U.container == correct.container
    
    def test_example_1(self):
        matrix = Matrix([[1, 2, 3], [2, 3, 1], [-2, 3, -2]])
        L, U = matrix.alu_factorization()
        L_correct = Matrix([[1, 0, 0], [2, 1, 0], [-2, -7, 1]])
        U_correct = Matrix([[1, 2, 3], [0, -1, -5], [0, 0, -31]])
        print(L)
        print(U)
        assert L.container == L_correct.container
        assert U.container == U_correct.container

class TestALU_Solve:

    def test_example_1(self):
        A = Matrix([[1, 2], [4, 9]])
        b = Matrix([5, 21])
        x = A.alu_solve(b)
        answer = Matrix([3, 1])
        assert x.container == answer.container