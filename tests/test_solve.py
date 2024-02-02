import pytest
from linear_algebra.basic import Matrix, MatrixInitializationError

class Rearrange:

    def test_vector(self):
        vector = Matrix([4, 3, 2, 1])
        correct_vector = Matrix([1, 2, 3, 4])
        assert(vector.container == correct_vector.container)
    
    