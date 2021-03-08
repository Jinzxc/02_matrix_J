import math

from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 200, 0, 0 ]
t_matrix = new_translation_matrix()
matrix = []

# Matrix Testing Start #
print('Testing add_edge. Adding (1, 2, 3), (4, 5, 6) m2 =')
add_edge(matrix, 1, 2, 3, 4, 5, 6)
print_matrix(matrix)
print()

print('Testing ident. m1 =')
ident(t_matrix)
print_matrix(t_matrix)
print()

print('Testing Matrix mult. m1 * m2 =')
matrix_mult(t_matrix, matrix)
print_matrix(matrix)
print()

print('Testing Matrix mult. m1 =')
m1 = []
add_edge(m1, 1, 2, 3, 4, 5, 6)
add_edge(m1, 7, 8, 9, 10, 11, 12)
print_matrix(m1)
print()

print('Testing Matrix mult. m1 * m2 =')
matrix_mult(m1, matrix)
print_matrix(matrix)
print()

print('Testing Matrix mult. m1 =')
t_matrix = rotateZMatrix(-10)
print_matrix(t_matrix)
print()

print('Testing Matrix rot. m1 * m2 =')
matrix_mult(t_matrix, matrix)
print_matrix(matrix)
print()

print('Testing Matrix shift m2 + (d10, d10) =')
shift(matrix, 10, 10)
print_matrix(matrix)
print()

# Matrix Testing End #

draw_matrix = []

for i in range(0, 730, 5):
    radians = i * (math.pi / 180)
    r1 = 100 * (1 - math.sin(radians))
    r2 = 100 * (1 - math.sin(radians + math.pi/36))

    x1 = r1 * math.cos(radians)
    y1 = r1 * math.sin(radians)

    x2 = r2 * math.cos(radians + math.pi/36)
    y2 = r2 * math.sin(radians + math.pi/36)

    add_edge(draw_matrix, int(x1), int(y1), 0, int(x2), int(y2), 0)

shift(draw_matrix, 250, 250)

for i in range(100):
    draw_lines( draw_matrix, screen, color )
    matrix_mult(t_matrix, draw_matrix)
    shift(draw_matrix, 100, 0)
    color[1] += 4

save_extension(screen, 'Rising_Loong_.png')
display(screen)
