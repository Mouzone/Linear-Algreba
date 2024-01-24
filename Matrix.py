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
        if check(user_input):
            self.container = user_input
            self.height = len(user_input)
            self.width = len(user_input[0])
    
    def check(user_input):
        # check if the user_input is a list
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
        return [element for sublist in self.container for element in sublist]

    def print():
        for i in range(len(container)):
            for j in range(len(conatiner[0])):
                print(container[i][j] + ' ')
            print('\n') 

    # Arithmetic operations
    def __add__(self, other):
        return

    def __sub__(self, other):
        return 

    def __mul__(self, other):
        return 
