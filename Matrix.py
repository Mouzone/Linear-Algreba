class Matrix:
    # empty matrix
    def init():
        self.container = []
        self.height = 0
        self.width = 0

    # add a function to check the user input
    # [0] vs [[0]]
    # column vector is [[0],[1],[2]], row vector is [[1,2,3]]
    def init(user_input):
        if check_init(user_input):
            self.container = user_input
            self.height = len(user_input)
            self.width = len(user_input[0])
    
    def check_init(user_input):
        # check if the user_input is a list
        if not is_instance(user_input, list):
            return False

        # check if all rows are lists
        for i in range(len(user_input)):
            if not is_instance(user_input, list):
                return False
                
        # check all lists are the same length
        # return the row position that is not a good length
        for i in range(1, len(user_input)):
            if len(user_input[i]) != len(user_input[i-1]):
                return False

        # check all elements are ints
        # return position of not int in error message
        for i in range(len(user_input)):
            for j in range(len(user_input[0])):
                if not isinstance(user_input[i][j], int):
                    return False

    def flatten():
        return [element for row in self.container for element in row]

    def print():
        for i in range(self.height):
            for j in range(len(self.width)):
                print(container[i][j] + ' ')
            print('\n') 

    def check_before_operations(other):
        if self.height != other.height:
            return False
        elif self.width != other.width:
            return False
        return True

    # Arithmetic operations------------------------------------------------------------------------------------------------------
    # combine add and subtract into one function
    def __add__(self, other):
        if check_before_operations(other):
            result = [[] for i in range(self.height)]
            for i in range(len(self.height)):
                for j in range(len(self.width)):
                    result[i].append(self.container[i][j] + other.container[i][j])

            result = Matrix(result)
            return result

    def __sub__(self, other):
        if check_before_operations(other):
            result = [[] for i in range(self.height)]
            for i in range(len(self.height)):
                for j in range(len(self.width)):
                    result[i].append(self.container[i][j] - other.container[i][j])

            result = Matrix(result)
            return result 

    def __mul__(self, other):
        return 