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
    def check_before_operations(other):
        if self.height != other.height:
            return False
        elif self.width != other.width:
            return False
        return True
    
    # combine add and subtract into one function
    def __add__(self, other):
        if check_before_operations(other):
            result = [[] for i in range(self.height)]
            for i in range(self.height):
                for j in range(self.width):
                    result[i].append(self.container[i][j] + other.container[i][j])

            result = Matrix(result)
            return result

    def __sub__(self, other):
        if check_before_operations(other):
            result = [[] for i in range(self.height)]
            for i in range(self.height):
                for j in range(self.width):
                    result[i].append(self.container[i][j] - other.container[i][j])

            result = Matrix(result)
            return result 

    def __mul__(self, other):
        return 
