class MatrixInitializationError(Exception):
    pass

class Matrix:
    
    # rewrite for the case of [[1], [2], [3]] which is a vector 
    def __init__(self, user_input):
        error = self.check_init(user_input)
        if error is not None:
            raise MatrixInitializationError(f"Matrix Initialization Error: {error}")

        if len(user_input[0]) > 1:
            self.create_matrix(user_input)
        else:
            self.create_vector(user_input)

    def create_matrix(self, user_input):
        self.container = user_input
        self.height = len(user_input)
        self.width = len(user_input[0])

    def create_vector(self, user_input):
        if len(user_input[0]) != 1:
            self.container = [[value] for value in user_input]
        else:
            self.container = user_input

        self.height = len(user_input)
        self.width = 1

    def check_init(self, user_input):
        # check it is not [] or [[]]
        if not isinstance(user_input, list) or not user_input or not user_input[0]:
            return "Matrix must be initialized with a non-empty list"

        if isinstance(user_input[0], list):
            return self.check_matrix(user_input)
        elif isinstance(user_input[0], int):
            return self.check_vector(user_input)
        else:
            return "Invalid matrix initialization"

    def check_matrix(self, user_input):
        all_list = self.check_all_type_list(user_input)
        if all_list is not None:
            return all_list
        return self.check_all_same_lengths(user_input)

    def check_all_type_list(self, user_input):
        for i, row in enumerate(user_input, 1):
            if not isinstance(row, list):
                return f"Row {i} is not a list"
        return self.check_all_ints(user_input)

    def check_all_same_lengths(self, user_input):
        for i in range(1, len(user_input)):
            if len(user_input[i]) != len(user_input[i - 1]):
                return f"Row {i + 1} has a different length than row {i}"
        return None

    def check_all_ints(self, user_input):
        for i, row in enumerate(user_input, 1):
            for j, val in enumerate(row, 1):
                if not isinstance(val, int):
                    return f"Element at position ({i}, {j}) is not an integer"
        return None

# Misc utility functions-------------------------------------------------------------------------------------------------------
    
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
        if n < 0:
            raise MatrixInitializationError(f"Invalid Dimension")
        
        result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

        return Matrix(result)

# Arithmetic operations---------------------------------------------------------------------------------------------------------
   
    def check_before_operations(self, other):
        if self.height != other.height:
            raise MatrixInitializationError(f"Heights are incompatible")
        if self.width != other.width:
            raise MatrixInitializationError(f"Widths are incompatible")   
             
    def __add__(self, other):
        self.check_before_operations(other)
        result = [
            [self.container[i][j] + other.container[i][j] for j in range(self.width)]
            for i in range(self.height)
        ]
        return Matrix(result)

    def __sub__(self, other):
        self.check_before_operations(other)
        result = [
            [self.container[i][j] - other.container[i][j] for j in range(self.width)]
            for i in range(self.height)
        ]
        return Matrix(result)

    def check_mul(self, other):
        if self.width != other.height:
            raise MatrixInitializationError(f"Dimensions are incompatible")   

    # write the case when it is a constant on either side
    def __mul__(self, other):
        # self and other are matrices
        # matrix_1 row i_1 * matrix_2_transposed row i_1 ...
        if isinstance(self, Matrix) and isinstance(other, Matrix):

            self.check_mul(other)
            other_transpose = other.transpose()
            result = [[0 for _ in range(other_transpose.height)] for _ in range(self.height)]

            for i in range(self.height):

                for j in range(other_transpose.height):

                    multiplied_values = [x * y for x, y in zip(self.container[i], other_transpose.container[j])]
                    val = sum(multiplied_values)
                    result[i][j] = val


        # matrix then int or float
        elif isinstance(other, int) or isinstance(other, float):
            result = []

            for i in range(self.height):
                result.append([other * val  for val in self.container[i]])

        else:
            raise MatrixInitializationError(f"Types are incompatible")   

        return Matrix(result)

    def __rmul__(self, other):
        # int or float then matrix
        result = []
        if (isinstance(other, int) or isinstance(other, float)) and isinstance(self, Matrix):
            for i in range(self.height):
                result.append([other * val for val in self.container[i]])

            return Matrix(result)
        raise MatrixInitializationError(f"Types are incompatible")   

# Advanced operations----------------------------------------------------------------------------------------------------------
   
    # transpose and inverse
    def transpose(self):
        if self.width == 0:
            return Matrix([[]])

        result = [[0 for _ in range(self.height)] for _ in range(self.width)]
        for i in range(self.height):
            for j in range(self.width):
                result[j][i] = self.container[i][j]

        return Matrix(result)

    def solve(self, target):
        # target must 
        if not isinstance(self, Matrix) or not isinstance(target, Matrix):
            raise ("Inputs must be type Matrices")
        if target.width != 1:
            raise ("Target must be a vector or a matrix of width 1")
        
        return

    # for inverse [[5] is [[1/5]]] bc I = [1]
    def inverse(self):
        return 
