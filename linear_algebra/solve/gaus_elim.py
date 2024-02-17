from linear_algebra.matrix import Matrix, MatrixInitializationError
class Aug_matrix:
    def __init__(self, A, b):
        check_input(A, b)
        self.container = [A.container[i] + b.container[i] for i in range(A.height)]
        self.height = A.height
        self.border = A.width
        self.rref = None
        self.solution = None

    def gaussian_elimination(self):
        for i in range(self.height):
            self.container = Matrix.rearrange_rows(self, i)
            self.container = Matrix.reduce(self, i)

            if Matrix.check_finished(self, self.border):
                self.rref = Matrix([row[border: ] for row in self.container])
                break
        
        self.rref = self.container
        if check_finished(self):
            self.solution = Matrix([row[border: ] for row in self.container])
        else:
            # figure out how to return solution when it is not unique
            return
        
        return 

def rearrange_rows(input_matrix, start):
    result = input_matrix.container
    iterations = min(input_matrix.height, input_matrix.width)

    for i in range(start, iterations):
        largest = input_matrix.container[i]
        for j in range(i, input_matrix.height):
            if abs(largest[i]) < abs(input_matrix.container[j][i]):
                largest = input_matrix.container[j]
            elif abs(largest[i]) == abs(input_matrix.container[j][i]):
                for k in range(i+1, input_matrix.width):
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

def check_input(A, b):
    if not (isinstance(A, Matrix) or isinstance(b, Matrix)):
        raise MatrixInitializationError(f"Inputs must be Matrices")
    if A.height != b.height:
        raise MatrixInitializationError(f"Dimensions are not compatible")

    return

def check_finished(input_matrix):
    # it is done if everything is 0 and diagonal is 1
    # it is also done if pivots are 1 and everything else is 0 
    for i in range(input_matrix.border):
        for  j in range(i+1):
            if i == j:
                if input_matrix.container[i][j] != 1:
                    return False
            else:
                if input_matrix.container[i][j] != 0:
                    return False

    return True