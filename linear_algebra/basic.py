class MatrixInitializationError(Exception):
    pass

class Matrix:
    
    # rewrite for the case of [[1], [2], [3]] which is a vector 
    def __init__(self, user_input):
        error = self.check_init(user_input)
        if error:
            raise MatrixInitializationError(f"Matrix Initialization Error: {error}")

        if isinstance(user_input[0], int):
            self.create_vector(user_input)
        else:
            self.create_matrix(user_input)

    def create_matrix(self, user_input):
        self.container = user_input
        self.height = len(user_input)
        self.width = len(user_input[0])

    def create_vector(self, user_input):
        self.container = [[value] for value in user_input]
        self.height = len(user_input)
        self.width = 1

    def check_init(self, user_input):
        if not isinstance(user_input, list) or not user_input:
            return "Matrix must be initialized with a non-empty list"

        if isinstance(user_input[0], list):
            return self.check_matrix(user_input)
        elif isinstance(user_input[0], int):
            return self.check_all_ints(user_input)
        else:
            return "Invalid matrix initialization"

    def check_matrix(self, user_input):
        all_list = self.check_all_type_list(user_input)
        if all_list is not None:
            return all_list
        return self.check_all_same_lengths(user_input)

    def check_all_type_list(self, user_input):
        for row in range(len(user_input)):
            if not isinstance(user_input[row], list):
                return f"Row {row + 1} is not a list"
            all_ints = self.check_all_ints(user_input[row])
            if all_ints:
                return all_ints
        return None

    def check_all_same_lengths(self, user_input):
        if len(user_input[0]) == 0:
            return "Matrix must be initialized with a non-empty list"

        for row in range(1, len(user_input)):
            if len(user_input[row]) != len(user_input[row - 1]):
                return f"Row {row + 1} has a different length than row {row}"
        return None

    def check_all_ints(self, user_input):
        for col in range(len(user_input)):
            if not isinstance(user_input[col], int):
                return f"Must be all integers"
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
    # add an inplace parameter
    def transpose(self):
        if self.width == 0:
            return Matrix([[]])

        result = [[0 for _ in range(self.height)] for _ in range(self.width)]
        for i in range(self.height):
            for j in range(self.width):
                result[j][i] = self.container[i][j]

        return Matrix(result)

    def rearrange_rows(input_matrix, separating_line):
        result = input_matrix.container
        iterations = min(input_matrix.height, separating_line)

        for i in range(iterations):
            largest = input_matrix.container[i]
            for j in range(i, input_matrix.height):
                if abs(largest[i]) < abs(input_matrix.container[j][i]):
                    largest = input_matrix.container[j]
                elif abs(largest[i]) == abs(input_matrix.container[j][i]):
                    for k in range(i+1, separating_line):
                        if largest[k] < input_matrix.container[j][k]:
                            largest = input_matrix.container[j]
                            break
            
            result.remove(largest)
            result.insert(i, largest)
        
        return Matrix(result)

    def reduce(input_matrix, start):
        result = input_matrix.container
        to_divide = input_matrix[start][start]
        result[start] = [element/to_divide for elment in result[start]]
        
        for i in range(start + 1, len(result)):
            list_to_subtract = [result[i][start] * element for element in result[start]]
            result[i] = [element_1 - element_2 for element_1, element_2 in zip(result[i], list_to_subtract)]

        return Matrix(result)

    def solve(self, target):
        if not isinstance(target, Matrix):
            raise MatrixInitializationError("Target must be Matrix")
        elif self.height != target.height:
            raise MatrixInitializationError("Dimensions are incompatible")

        problem_matrix = self.append(target)
        separating_line = self.width

        rearrage_rows(problem_matrix, separating_line)
        reduce(problem_matrix, row)
        # one function to check for rearrange rows
        ## add tests for matrices that are appeneded or really just a width that is less than the full width of the matrix
        # one function to figure out the multiplier and do the subtraction
        # one more to check if there is a row of all zeros, either at the end or after each operation
        # one more function to check if pivots along diagonal to exit early



        return

    # for inverse [[5] is [[1/5]]] bc I = [1]
    # add an inplace parameter
    def inverse(self):
        return 
