class Matrix:
    def __init__(self, user_input):
        check_input(user_input)

        if check_matrix(user_input):
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
    if not isinstance(user_input, list): # must be a list
        raise "Matrix Initialization Error: Invalid Container"
    if not all(isinstance(row, list) for row in user_input) and not all(isinstance(row, (int, float)) for row in user_input): # must be a list of lists or list of numbers
        raise "Matrix Initialization Error: Matrix must be a list of lists or list of ints or floats"
    return 

# we know that it is either a list of lists or a list of all numbers
def check_matrix(user_input):
    # check all rows same length and greater than 0 length
    if all(isinstance(row, (int, float)) for row in user_input):
        return False # for its a vector
    # we are left with only list elements inside the user_input

    sublist_lengths = [len(sublist) for sublist in user_input]
    if len(sublist_lengths) > 0 and len(set(sublist_lengths)) == 1:
        return True  # for its a matrix
    else:
        raise "Matrix Initialization Error: Lengths of each row must be greater than 0 and all the same length"

    if any(isinstance(row[0], list) for row in user_input):
        raise "Matrix Initialization Error: Excessive Nesting"
    
def check_add_sub(left, right):
    if left.height != right.height:
        raise "Matrix Initialization Error: Heights are incompatible"
    if left.width != right.width:
        raise "Matrix Initialization Error: Heights are incompatible"

def check_mul(left, right):
    # self will always be a matrix

    # takes care of matrix matrix
    if isinstance(right, Matrix):
        if left.width != right.height:
            raise "Matrix Initialization Error: Heights are incompatible"
        else:
            return True

    # this is for number * matrix or matrix * number
    if not (isinstance(right, int) or isinstance(right, float)):
        raise "Matrix Initialization Error: Heights are incompatible"
    else:
        return True
