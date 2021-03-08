"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    if len(matrix) < 1:
        print('Give me an actual matrix')
        return

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            print(matrix[j][i], end = ' ')
        print()

#turn the parameter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j == i:
                matrix[i][j] = 1

#returns a rotation matrix
def rotateZMatrix(degree):
    c = math.cos(degree * math.pi/180)
    s = math.sin(degree * math.pi/180)
    return [[c,-s, 0, 0],
            [s, c, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]]

#shifts the x and y of a matrix
def shift(matrix, x, y):
    for i in range(len(matrix)):
        matrix[i][0] += x
        matrix[i][1] += y

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    if not len(m1) == len(m2[0]):
        print('Cannot multiply these two matrices')
        return

    temp = []
    for i in range(len(m2)):
        temp.append([])
        for j in range(len(m2[0])):
            temp[i].append(m2[i][j])

    for row in range(len(m1[0])):
        for col in range(len(m2)):
            sum = 0
            for i in range(len(m1)):
                sum += m1[i][row] * temp[col][i]
            
            m2[col][row] = int(sum)
    return m2

def new_translation_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
