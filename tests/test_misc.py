import pytest

# flatten, print
import re
from linear_algebra.basic_operations import Matrix, MatrixInitializationError

class TestClass:
    def test_flatten(self):
        matrix = Matrix([])
        assert matrix.flatten == []

    def test_print(self):
        return