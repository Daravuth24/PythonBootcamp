from numpy import *


def matrix_addition(x, y):

    m1 = matrix(x)

    m2 = matrix(y)

    if len(x) == len(y):

        m3 = m1 * m2

        print(f"\nMatrix 1: \n \n{m1} \n")

        print(f"Matrix 2: \n \n {m2} \n")

        print(f"The result matrix is: \n \n{m3}")

    else:
        print("Error")


matrix_addition('3 7 5; 2 6 7; 4 3 2', '6 5 4; 3 2 1; 1 2 3')