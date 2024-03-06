# Linear Algebra Library

## Description
  This library is an application of the methods taught by Dr. Strang teaches in _Introduction to Linear Algebra_ while also applying my Python expertise. It is intended to be a more intuitive matrix-focused object-oriented approach than `NumPy`. 
  Currently facing the challenge of making it inutive enough for use in other fields, while also accounting for all edge cases and staying true to the core of Dr. Strang's teachings. 

## Install and Run
  There is a minor requirement of `pytest` and `re` if you want to go through the test cases, else there are no required dependencies

## Usage
### `Matrix` object
A `Matrix` object is the very core of this library. The methods are:
- transpose (x.transpose())
- flatten (reduce a matrix row of values) (x.flatten)

Operations included are:
- addition (+ operator)
- subtraction (- operator)
- multiplication (with constants and with other matrices) (* operator)
- printing as a string (standard built-in print() function)
  
Instantiation (Matrix):
<img width="297" alt="Screenshot 2024-03-05 at 8 43 04 PM" src="https://github.com/Mouzone/Linear-Algreba/assets/56100404/8b6b1f19-95f0-4272-bd24-1871b1e94241">

Instantiation (Vector):
<img width="184" alt="Screenshot 2024-03-05 at 8 44 22 PM" src="https://github.com/Mouzone/Linear-Algreba/assets/56100404/360dbb2e-fe66-4a38-8f38-db2e7802b762">
### Solve Subpackage
#### alu
Implements A=LU factorization to solve for the linear combination of the column vectors of a given vector(A) that results in another given vector(b).Follows the algorithm laid out by Dr. Strang that seeks to reduce a matrix to the product of a lower triangular matrix and upper triangular matrix. The algorithm can be seen in _Introduction to Linear Algebra_ on page 100. The contraints are that A must be `invertible` and b must be a `vector`(matrix with only one column).
<img width="216" alt="Screenshot 2024-03-05 at 8 50 28 PM" src="https://github.com/Mouzone/Linear-Algreba/assets/56100404/68331049-c82a-4e23-811b-a572ad00a9a0">

#### Gaussian Elimination
Implements the basic Gaussian Elimination in a brute force fashion as taugh in standard Linear Algebra courses. You must instantiate an `Aug_matrix`object with two `Matrix` objects: A and b. The gaussian_elimination() method is then called as a class method to mimic the matrix appending done on pen and paper. Works with integer and float values for input, but the output will always be float due to use of the division operator.
<img width="245" alt="Screenshot 2024-03-05 at 8 53 59 PM" src="https://github.com/Mouzone/Linear-Algreba/assets/56100404/31fef120-c857-4449-ae86-e390bf73f798">


  
