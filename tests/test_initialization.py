import pytest
from linear_algebra.basic_operations import Matrix

class TestClass:
    def test_empty_matrix(self):
    # Test creation of an empty matrix
        matrix = Matrix()
        assert matrix.container == []
        assert matrix.height == 0
        assert matrix.width == 0
    
    def test_user_input(self):
        matrix = Matrix([[0]])
        assert matrix.container == [[0]]
        assert matrix.height == 1
        assert matrix.width == 1
    
    # def test_user_input([[0]]):

    # def test_user_input([[1,0], [0,1]]):

    # def test_user_input([[1,2,3], [4,5,6]]):

    # def test_user_input([[1,2,3], [1, 2]]):

    # def test_user_input([['dog'], ['cat']]):

