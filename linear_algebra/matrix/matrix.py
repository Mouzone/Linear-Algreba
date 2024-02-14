class MatrixInitializationError(Exception):
    pass

class Matrix:
    
    # rewrite for the case of [[1], [2], [3]] which is a vector 
    def __init__(self, user_input):
        error = self.check_init(user_input)
        if error:
            raise MatrixInitializationError(f"Matrix Initialization Error: {error}")

        if isinstance(user_input[0], int) or isinstance(user_input[0], float):
            self.create_vector(user_input)
        else:
            self.create_matrix(user_input)

    ## make a general function fro creating, and call it with a keyword and input the values
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


    def check_init(self, user_input):
        if not isinstance(user_input, list) or not user_input:
            return "Matrix must be initialized with a non-empty list"

        if isinstance(user_input[0], list):
            return self.check_matrix(user_input)
        elif isinstance(user_input[0], int) or isinstance(user_input[0], float):
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
            if not isinstance(user_input[col], int) and not isinstance(user_input[col], float):
                return f"Must be all integers"
        return None