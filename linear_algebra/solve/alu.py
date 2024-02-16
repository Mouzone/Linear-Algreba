# rewrite such that these are not class functions but general functions that take input
# not .functions anymore
# returns error if it doesn't factor all the way with the check

# input must be an invertible matrix, until invertibility check is found
def alu_factorization(A):
    U = Matrix(A.container.copy())
    L = Matrix.identity_matrix(copy.width)

    for i in range(U.height):
        for  j in range(i):
            if U.container[j][j] != 0 and U.container[i][j] != 0:
                multiplier = -U.container[i][j]/U.container[j][j]
                L.container[i][j] = U.container[i][j]/U.container[j][j]
                U.container[i] = [U.container[i][pos] + multiplier * U.container[j][pos] for pos in range(U.width)]

    return L, U #result is L, copy is U
            
def input_check(A, b):
    if not isinstance(b, Matrix):
        raise MatrixInitializationError("Target must be Matrix")
    elif A.height != b.height:
        raise MatrixInitializationError("Dimensions are incompatible")
    elif A.height != A.width:
        raise MatrixInitializationError("Matrix must be invertible")

# input must be an invertible matrix, until invertibility check is found
## can check for inveritbiltiy here, bc if encounter any 0 rows then it is not invertible in the U
def alu_solve(A, b):
    input_check(A, B)

    L, U = alu_factorization(A)

    # user forward substitution from top to bottom to find 'c'
    c = [0 for _ in range(L.width)]
    for row in range(L.height):
        c[row] = target.container[row][0] - sum([c[col] * L.container[row][col] for col in range(L.width)])
    
    # solving by backwards plugging
    answer = [0 for _ in range(U.height)]
    for row in range(U.height - 1, -1, -1):
        answer[row] = c[row] - sum([answer[col] * U.container[row][col] for col in range(U.width)])
    
    return Matrix(answer)