   # input must be an invertible matrix, until invertibility check is found
    def alu_factorization(self):
        copy = Matrix(self.container.copy())
        result = Matrix.identity_matrix(copy.width)

        for i in range(copy.height):
            for  j in range(i):
                if copy.container[j][j] != 0 and copy.container[i][j] != 0:
                    multiplier = -copy.container[i][j]/copy.container[j][j]
                    result.container[i][j] = copy.container[i][j]/copy.container[j][j]
                    copy.container[i] = [copy.container[i][pos] + multiplier * copy.container[j][pos] for pos in range(copy.width)]
                # if not Matrix.check_finished(copy):
                #     break

        return result, copy #result is L, copy is U
                

    # input must be an invertible matrix, until invertibility check is found
    ## can check for inveritbiltiy here, bc if encounter any 0 rows then it is not invertible in the U
    def alu_solve(self, target):
        if not isinstance(target, Matrix):
            raise MatrixInitializationError("Target must be Matrix")
        elif self.height != target.height:
            raise MatrixInitializationError("Dimensions are incompatible")
        elif self.height != self.width:
            raise MatrixInitializationError("Matrix must be invertible")

        L, U = self.alu_factorization()

        # user forward substitution from top to bottom to find 'c'
        c = [0 for _ in range(L.width)]
        for row in range(L.height):
            c[row] = target.container[row][0] - sum([c[col] * L.container[row][col] for col in range(L.width)])
        
        # solving by backwards plugging
        answer = [0 for _ in range(U.height)]
        for row in range(U.height - 1, -1, -1):
            answer[row] = c[row] - sum([answer[col] * U.container[row][col] for col in range(U.width)])
        
        return Matrix(answer)