from linear_algebra.matrix.matrix import Matrix

def identity_matrix(n):
    if n > 0:
        return Matrix([[1 if i == j else 0 for j in range(n)] for i in range(n)])
    
    raise MatrixInitializationError(f"Invalid Dimension")