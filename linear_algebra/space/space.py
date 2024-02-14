# nullspace including special vectors
# rank, cokumn space, lienar independence
# vector space for col space and null space
def null_space(self):
    zero_vector = Matrix([[0] for i in self.height])
    original = Matrix(self.container.copy())
    columns = original.transpose()
    # reduces it to 
    rref = alu_solve(self, zero_vector)
    
    # check each column if its a pivot column
    
# take a list of inputs what they want, if no iunputs we find all the spaces and return them