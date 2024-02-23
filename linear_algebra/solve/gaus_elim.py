from linear_algebra.matrix import Matrix, MatrixInitializationError
from linear_algebra.utility import *

class Aug_matrix:
    def __init__(self, A, b):
        check_input(A, b)
        self.A = A
        self.b = b
        self.container = [A.container[i] + b.container[i] for i in range(A.height)]
        self.height = A.height
        self.border = A.width
        self.rref = None
        self.solution = None

    def gaussian_elimination(self):

        for i in range(self.height):
            self.container = rearrange_rows(self, i)
            self.container = reduce(self, i)

            if check_upper_triangular(self):
                break
        
        # self.container should now be in rref form
        self.rref = [row[:self.border] for row in self.container]
        # return the basis of the solution space
        if check_unique(self.rref): # no free variables, square matrix
            self.solution = Matrix([row[self.border:] for row in self.container]).transpose()
            return "Unique"
        else:
            self.solution = list(find_special_solutions(self))
            self.solution = [Matrix(solution).transpose() for solution in self.solution]
            return "Not Unique" 

def rearrange_rows(input_matrix, start):
    result = input_matrix.container
    iterations = min(input_matrix.height, input_matrix.border)

    for i in range(start, iterations):
        largest = input_matrix.container[i]
        for j in range(i, input_matrix.height):
            if abs(largest[i]) < abs(input_matrix.container[j][i]):
                largest = input_matrix.container[j]
            elif abs(largest[i]) == abs(input_matrix.container[j][i]):
                for k in range(i+1, input_matrix.border):
                    if largest[k] < input_matrix.container[j][k]:
                        largest = input_matrix.container[j]
                        break
        
        result.remove(largest)
        result.insert(i, largest)
    
    return result

def reduce(input_matrix, start):
    result = input_matrix.container
    to_divide = result[start][start]
    result[start] = [element/to_divide for element in result[start]]

    for i in range(len(result)):
        if i != start:
            list_to_subtract = [result[i][start] * element for element in result[start]]
            result[i] = [element_1 - element_2 for element_1, element_2 in zip(result[i], list_to_subtract)]

    return result

def find_special_solutions(input_matrix):
    return 

def check_input(A, b):
    if not (isinstance(A, Matrix) or isinstance(b, Matrix)):
        raise MatrixInitializationError(f"Inputs must be Matrices")
    if A.height != b.height:
        raise MatrixInitializationError(f"Dimensions are not compatible")
    return

# returns true if it is upper triangular (so unique and singular matrices return once pivots reduce to 1
# fails it is not square since the border is only n, but we should check the m rows when m > n
def check_upper_triangular(input_matrix):
    # it is done if everything is 0 and diagonal is 1
    # it is also done if pivots are 1 and everything else is 0 
    iterations = min(input_matrix.height, input_matrix.border)
    for i in range(iterations):
        for  j in range(i+1):
            if i == j:
                # if the diagonal is not reduced to 1s for pivots or 0s if it is a zero row
                if input_matrix.container[i][j] != 1 or input_matrix.container[i][j] != 0:
                    return False
            else:
                # if it is not a upper yet
                if input_matrix.container[i][j] != 0:
                    return False

    return True

def check_unique(A, tolerance=1e-9):
    # id_matrix = identity_matrix(len(A))
    # use epsilon function to check values against the tolerance
    # return all(all(abs(val1 - val2) < tolerance for val1, val2 in zip(row1, row2)) for row1, row2 in zip(A, id_matrix.container))
    for i in range(len(A)):
        for j in range(len(A)):
            if j == i:
                if A[i][j] - 1 > tolerance:
                    return False
            else:
                if A[i][j] - 0 > tolerance:
                    return False

    return True
