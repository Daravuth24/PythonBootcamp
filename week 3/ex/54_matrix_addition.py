from numpy import *


def matrix_addition(x, y):

    m1 = matrix(x)

    m2 = matrix(y)

    m3 = m1 + m2

    print(f"\nMatrix 1: \n \n{m1} \n")

    print(f"Matrix 2: \n \n {m2} \n")

    print(f"The result matrix is: \n \n{m3}")


matrix_addition('10 5 4 2; 5 0 9 5; 9 19 60 8; 7 8 4 5', '12 65 34 42; 10 5 89 45; 11 21 63 78; 87 78 54 65')
