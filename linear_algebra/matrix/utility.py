def flatten(self):
    return [element for row in self.container for element in row]

def identity_matrix(n):
    if n > 0:
        return Matrix([[1 if i == j else 0 for j in range(n)] for i in range(n)])
    
    raise MatrixInitializationError(f"Invalid Dimension")