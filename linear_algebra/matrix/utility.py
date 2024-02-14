    def flatten(self):
        return [element for row in self.container for element in row]

    # somehow make it so when matrice output there are large brackets 
    def __str__(self):
        matrix_str = ""
        for i in range(self.height):
            for j in range(self.width):
                matrix_str += str(self.container[i][j])
                if j < self.width - 1:  # Add space if it's not the last element in the row
                    matrix_str += ' '
            if i < self.height - 1:  # Add newline if it's not the last row
                matrix_str += '\n'
        return matrix_str
   
    def identity_matrix(n):
        if n > 0:
            return Matrix([[1 if i == j else 0 for j in range(n)] for i in range(n)])
        
        raise MatrixInitializationError(f"Invalid Dimension")

    # appends for solving and inverting such that those of the same rows become the same rows
    def append(self, other):
        if isinstance(self, Matrix) and isinstance(other, Matrix):
            if self.height == other.height:
                return Matrix([left + right for left, right in zip(self, other)])
            raise MatrixInitializationError("Heights are incompatible")
        raise MatrixInitializationError("Inputs must be Matrices")
