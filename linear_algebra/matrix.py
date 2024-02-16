class MatrixInitializationError(Exception):
    pass

class Matrix:
    def __init__(self, user_input):
        error = self.validate_input(user_input)
        if error:
            raise MatrixInitializationError(f"Matrix Initialization Error: {error}")
        self.create_matrix(user_input) if isinstance(user_input[0], list) else self.create_vector(user_input)

    def create_matrix(self, user_input):
        self.container = user_input
        self.height = len(user_input)
        self.width = len(user_input[0])
        self.rref = None

    def create_vector(self, user_input):
        self.container = [[value] for value in user_input]
        self.height = len(user_input)
        self.width = 1
        self.rref = None

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.container)

    def flatten(self):
        return [element for row in self.container for element in row]

    def validate_input(self, user_input):
        if not isinstance(user_input, list) or not user_input:
            return "Matrix must be initialized with a non-empty list"
        if isinstance(user_input[0], list):
            return self.validate_matrix(user_input)
        elif not all(isinstance(val, (int, float)) for val in user_input):
            return "Vector must contain only numbers"
        return None

    def validate_matrix(self, user_input):
        for row in user_input:
            if not isinstance(row, list):
                return "Matrix must be a list of lists"
            if not row:
                return "Matrix must not contain empty rows"
            if not all(isinstance(val, (int, float)) for val in row):
                return "Matrix must contain only numbers"
            if len(row) != len(user_input[0]):
                return "All rows of the matrix must have the same length"
        return None

# Operations--------------------------------------------------------------------------------------------------------------------
    # rewrite the errror checking logic into somehting neater for mul and rmul
    
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
        result = []
        if (isinstance(other, int) or isinstance(other, float)) and isinstance(self, Matrix):
            for i in range(self.height):
                result.append([other * val for val in self.container[i]])
            return Matrix(result)
        raise MatrixInitializationError(f"Types are incompatible")   

    def transpose(self):
        if self.width == 0:
            return Matrix([[]])

        result = [[0 for _ in range(self.height)] for _ in range(self.width)]
        for i in range(self.height):
            for j in range(self.width):
                result[j][i] = self.container[i][j]

        return Matrix(result)