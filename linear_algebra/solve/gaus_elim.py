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

def check_finished(input_matrix, border):
    # it is done if everything is 0 and diagonal is 1
    # it is also done if pivots are 1 and everything else is 0 
    for i in range(border):
        for  j in range(i+1):
            if i == j:
                if input_matrix.container[i][j] != 1:
                    return False
            else:
                if input_matrix.container[i][j] != 0:
                    return False

    return True

def append(self, target):
    return Matrix([self.container[i] + target.container[i] for i in range(self.height)]), self.width

def gaussian_elimination(self, target, rref=False):
    # add logic to check conmpatibility
    augmented_matrix, border = Matrix.append(self, target)
    # rearrange
    # iterate by column
    for i in range(augmented_matrix.height):
        augmented_matrix = Matrix.rearrange_rows(augmented_matrix, i)
        augmented_matrix = Matrix.reduce(augmented_matrix, i)

        if Matrix.check_finished(augmented_matrix, border):
            return Matrix([row[border: ] for row in augmented_matrix.container])
            break

    return_items = []
    # save rref as something unique to each
    # same for nullspace, column space, rowspace as something unique to each matrix made
    # raise MatrixInitializationError(f"Types are incompatible")   

    # return_items if doesn't work then return the incomplete rref for cases like null space
    if rref:
        return_items.append(augmented_matrix)
    if Matrix.check_finished(augmented_matrix, border):
        return_items.append(Matrix([row[border: ] for row in augmented_matrix.container]))
    return return_items