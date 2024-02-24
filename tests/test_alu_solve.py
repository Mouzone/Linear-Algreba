import pytest
from linear_algebra.matrix import Matrix
from linear_algebra.solve.alu import alu_factorization, input_check, alu_solve
from linear_algebra import utility

class TestSolve_Requirements:
    def test_one_matrice(self):
        vector = Matrix([1, 2, 3, 4])

        with pytest.raises(MatrixInitializationError, match="Target must be Matrix"):
            alu_solve(vector, "dog")
    
    def test_heights_not_equal(self):
        matrix_1 = Matrix([[5, 2, 8], [1, 6, 3], [9, 4, 7], [2, 8, 1], [7, 3, 6], [4, 9, 5], [3, 1, 2], [6, 7, 4]]) 
        matrix_2 = Matrix([[5, 2, 8], [1, 6, 3], [9, 4, 7], [2, 8, 1], [7, 3, 6], [4, 9, 5], [3, 1, 2]])

        with pytest.raises(MatrixInitializationError, match="Dimensions are incompatible"):
            alu_solve(matrix_1, matrix_2)

class TestFactorization:

    def test_identity_matrix(self):
        matrix = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        L, U = alu_factorization(matrix)
        correct = utility.identity_matrix(3)
        assert L.container == correct.container
        assert U.container == correct.container
    
    def test_example_1(self):
        matrix = Matrix([[1, 2, 3], [2, 3, 1], [-2, 3, -2]])
        L, U = alu_factorization(matrix)
        L_correct = Matrix([[1, 0, 0], [2, 1, 0], [-2, -7, 1]])
        U_correct = Matrix([[1, 2, 3], [0, -1, -5], [0, 0, -31]])
        assert L.container == L_correct.container
        assert U.container == U_correct.container
    
    def test_singular_1(self):
        matrix = Matrix([[1,2,3], [2,4,6], [3,6,9]])
        L, U = alu_factorization(matrix)
        U_actual = Matrix([[1,2,3], [0,0,0], [0,0,0]])
        assert U.container == U_actual.container

class TestALU_Solve:

    def test_example_1(self):
        A = Matrix([[1, 2], [4, 9]])
        b = Matrix([5, 21])
        x = alu_solve(A, b)
        answer = Matrix([3, 1])
        assert x.container == answer.container