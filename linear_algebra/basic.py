class MatrixInitializationError(Exception):
    pass

class Matrix:
    # empty matrix
    def __init__(self, user_input=None):
        if user_input is None:
            self.container = [[]]
            self.height = 0
            self.width = 0
        else:
            self.check_init(user_input)
            self.container = user_input
            self.height = len(user_input)
            self.width = len(user_input[0])
    # support the creation of vevtors fast when the input is [1, 2,3]
    def create_vector(self, user_input):
        return
        
    def check_init(self, user_input):
        # check if the user_input is a list
        if not isinstance(user_input, list):
            raise MatrixInitializationError("Input must be a list of lists")
        
        if len(user_input) == 0 or not isinstance(user_input[0], list):
            raise MatrixInitializationError("Input must be a list of lists")

        # check if all rows are lists
        for i in range(len(user_input)):
            if not isinstance(user_input[i], list):
                raise MatrixInitializationError(f"Row {i+1} is not a list")

        # check all lists are the same length
        for i in range(1, len(user_input)):
            if len(user_input[i]) != len(user_input[i-1]):
                raise MatrixInitializationError(f"Row {i+1} has a different length than row {i}")

        # check all elements are ints
        for i in range(len(user_input)):
            for j in range(len(user_input[0])):
                if not isinstance(user_input[i][j], int):
                    raise MatrixInitializationError(f"Element at position ({i+1}, {j+1}) is not an integer")

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
    # for inverse [[5] is [[1/5]]] bc I = [1]
    def transpose(self):
        if self.width == 0:
            return Matrix([[]])

        result = [[0 for _ in range(self.height)] for _ in range(self.width)]
        for i in range(self.height):
            for j in range(self.width):
                result[j][i] = self.container[i][j]
        print(result)
        return Matrix(result)

    def inverse(self):
        return 
    
    def solve(self, target):
        # input must
        return