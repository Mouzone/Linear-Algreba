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
    
    def check_init(self, user_input):
        # check if the user_input is a list
        if not isinstance(user_input, list) or len(user_input) == 0:
            raise MatrixInitializationError("Input must be a non-empty list of lists")

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

    # write the case when it is a constant on either side
    def __mul__(self, other):
        return 

# advanced operations
    # transpose and inverse