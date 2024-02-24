class MatrixInitializationError(Exception):
    pass

# weridly initializes [[0,0,0,0]]
class Matrix:
    def __init__(self, user_input):
        error = check_input(user_input)
        if error:
            raise MatrixInitializationError(f"Matrix Initialization Error: {error}")
        if isinstance(user_input[0], list):
            self.create_container(user_input, False) 
        else:
            self.create_container(user_input, True)

    def create_container(self, user_input, isVector):
        if isVector:
            self.container = [[value] for value in user_input]
            self.width = 1 # has to manually set since integers do not have len function

        else:
            self.container = user_input
            self.width = len(user_input[0])

        self.height = len(user_input)

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.container)

    def flatten(self):
        return [element for row in self.container for element in row]

# Operations--------------------------------------------------------------------------------------------------------------------

    # is the function that addition and sub inherits from since both share the same code            
    def __add_sub(self, other, operation):
        check_add_sub(self, other)
        result = [
            [
                self.container[i][j] + other.container[i][j] if operation == "add" else self.container[i][j] - other.container[i][j]
                for j in range(self.width)
            ]
            for i in range(self.height)
        ]
        return Matrix(result)

    def __add__(self, other):
        return self.__add_sub(other, "add")

    def __sub__(self, other):
        return self.__add_sub(other, "sub")

    def __mul__(self, other):
        # self and other are matrices
        # matrix_1 row i_1 * matrix_2_transposed row i_1 ...
        check_mul(self, other)
        if isinstance(other, Matrix):
            other_transpose = other.transpose()

            result = [[0 for _ in range(other_transpose.height)] for _ in range(self.height)]
            for i in range(self.height):
                for j in range(other_transpose.height):
                    multiplied_values = [x * y for x, y in zip(self.container[i], other_transpose.container[j])]
                    val = sum(multiplied_values)
                    result[i][j] = val

        # matrix then int or float
        if isinstance(other, int) or isinstance(other, float):
            result = []
            for i in range(self.height):
                result.append([other * val  for val in self.container[i]])

        return Matrix(result)

    def __rmul__(self, other):
        check_mul(self, other)
        result = []
        for i in range(self.height):
            result.append([other * val for val in self.container[i]])
        return Matrix(result)

    def transpose(self):
        if self.width == 0:
            return Matrix([[]])

        result = [[0 for _ in range(self.height)] for _ in range(self.width)]
        for i in range(self.height):
            for j in range(self.width):
                result[j][i] = self.container[i][j]

        return Matrix(result)

def check_input(user_input):
    if not isinstance(user_input, list) or not user_input:
        return "Matrix must be initialized with a non-empty list"
    if isinstance(user_input[0], list):
        return check_matrix(user_input)
    # below validates vector
    elif not all(isinstance(val, (int, float)) for val in user_input):
        return "Vector must contain only numbers"
    return None

def check_matrix(user_input):
    # checking for the proper nesting 

    for row in user_input:
        if not isinstance(row, list):
            return "Matrix must be a list of lists"
        if not row:
            return "Matrix must not contain empty rows"
        if not all(isinstance(val, (int, float)) for val in row):
            return "Matrix must contain only numbers"
        if len(row) != len(user_input[0]):
            return "All rows of the matrix must have the same length"
        if any(isinstance(row[0], list)):
            return "Excessive nesting in the lists"
    return None
    
def check_add_sub(left, right):
    if left.height != right.height:
        return "Heights are incompatible"
    if left.width != right.width:
        return "Widths are incompatible"  

def check_mul(left, right):
    # self will always be a matrix

    # takes care of matrix matrix
    if isinstance(right, Matrix):
        if left.width != right.height:
            return "Dimensions are incompatible"
        else:
            return True

    # this is for number * matrix or matrix * number
    if not (isinstance(right, int) or isinstance(right, float)):
        return "Types are incompatible"  
    else:
        return True
