from linear_algebra.matrix import Matrix

def validate_input(user_input):
    if not isinstance(user_input, list) or not user_input:
        return "Matrix must be initialized with a non-empty list"
    if isinstance(user_input[0], list):
        return self.validate_matrix(user_input)
    elif not all(isinstance(val, (int, float)) for val in user_input):
        return "Vector must contain only numbers"
    return None

def validate_matrix(user_input):
    for row in user_input:
        if not isinstance(row, list):
            return "Matrix must be a list of lists"
        if not row:
            return "Matrix must not contain empty rows"
        if not all(isinstance(val, (int, float)) for val in row):
            return "Matrix must contain only numbers"
        if len(row) != len(user_input[0]):
            return "All rows of the matrix must have the same length"
    return None
    
def check_before_operations(left, right):
    if left.height != right.height:
        raise MatrixInitializationError(f"Heights are incompatible")
    if left.width != right.width:
        raise MatrixInitializationError(f"Widths are incompatible")   

def check_mul(left, right):
    # self will always be a matrix

    # takes care of matrix matrix
    if isinstance(right, Matrix):
        if left.width != right.height:
            raise MatrixInitializationError(f"Dimensions are incompatible")   
        else:
            return True

    # this is for number * matrix or matrix * number
    if not (isinstance(right, int) or isinstance(right, float)):
        raise MatrixInitializationError(f"Types are incompatible")   
    else:
        return True
