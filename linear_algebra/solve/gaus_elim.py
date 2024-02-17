# maybe make an augmented matrix class that inherits from matrix class
# only difference is it has a border attribute
# has a rref container as well
# make the class take an A and b matrix
# then call the function .guassian_elimination() to solve like sklearn calling fit_transform
from linear_algebra.matrix import Matrix, MatrixInitializationError
class Aug_matrix:
    def __init__(self, A, b):
        check_input(A, b)
        self.container = [A.container[i] + b.container[i] for i in range(A.height)]
        height = A.height
        border = A.width
        rref = None

    # return whatever the  thing at the end is even if it is not identity matrix
    # also be able to return the vectors like null space would return the free varaible vectors
    def gaussian_elimination(self):
        # add logic to check conmpatibility
        # rearrange
        # iterate by column
        for i in range(self.height):
            self.container = Matrix.rearrange_rows(self, i)
            self.container = Matrix.reduce(self, i)

            if Matrix.check_finished(self, border):
                return Matrix([row[border: ] for row in self.container])
                break

        return_items = []
        # save rref as something unique to each
        # same for nullspace, column space, rowspace as something unique to each matrix made
        # raise MatrixInitializationError(f"Types are incompatible")   

        # return_items if doesn't work then return the incomplete rref for cases like null space
        if rref:
            return_items.append(self)
        if Matrix.check_finished(self, border):
            return_items.append(Matrix([row[border: ] for row in self.container]))
        return return_items

# useless for now until implement gaussian elimination
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
    
    return Matrix(result)

# useless for now until implement gaussian elimination
def reduce(input_matrix, start):
    result = input_matrix.container
    to_divide = result[start][start]
    result[start] = [element/to_divide for element in result[start]]

    for i in range(len(result)):
        if i != start:
            list_to_subtract = [result[i][start] * element for element in result[start]]
            result[i] = [element_1 - element_2 for element_1, element_2 in zip(result[i], list_to_subtract)]

    return Matrix(result)

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