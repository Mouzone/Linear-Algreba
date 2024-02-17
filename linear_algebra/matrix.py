from linear_algebra import checks

class MatrixInitializationError(Exception):
    pass

class Matrix:
    def __init__(self, user_input):
        error = self.validate_input(user_input)
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
                
    def __add__(self, other):
        checks.check_before_operations(self, other)
        result = [
            [self.container[i][j] + other.container[i][j] for j in range(self.width)]
            for i in range(self.height)
        ]
        return Matrix(result)

    def __sub__(self, other):
        checks.check_before_operations(self, other)
        result = [
            [self.container[i][j] - other.container[i][j] for j in range(self.width)]
            for i in range(self.height)
        ]
        return Matrix(result)

    def __mul__(self, other):
        # self and other are matrices
        # matrix_1 row i_1 * matrix_2_transposed row i_1 ...
        checks.check_mul(self, other)
        if isinstance(self, Matrix) and isinstance(other, Matrix):
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
        checks.check_mul(self, other)
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
