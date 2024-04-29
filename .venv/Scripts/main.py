#188857 Marcin Araśniewicz
import numpy as np
from Matrix import Matrix
from Solving_Methods import SolvingMethods
from plot import Plot



if __name__ == "__main__":
    n = 957
    e = 8
    a1 = 5 + e
    a2 = a3 = -1
    f = 8
    b = [np.sin(i * (f + 1)) for i in range(n)]
    vector_b = Matrix(1, n, 0, 0, 0)
    vector_b.assign_values_to_vector(b)
    A = Matrix(n, n, a1, a2, a3)

    #jacobi_res_norm, jacobi_iterations, jacobi_time = SolvingMethods.jacobi(A, n, n, vector_b)
    #print(f"Jacobi: {jacobi_iterations} iterations, {jacobi_time} seconds")

    #gauss_res_norm, gauss_iterations, gauss_time = SolvingMethods.gauss_seidl(A, n, n, vector_b)
    #print(f"Gauss-Seidel: {gauss_iterations} iterations, {gauss_time} seconds")

    #Plot.make_plot_norms(jacobi_iterations, jacobi_res_norm, gauss_iterations, gauss_res_norm)

    #equation number 2
    a1 = 3
    a2 = a3 = -1
    n = 957
    f = 8
    b = [np.sin(i * (f + 1)) for i in range(n)]
    vector_b = Matrix(1, n, 0, 0, 0)
    vector_b.assign_values_to_vector(b)
    A = Matrix(n, n, a1, a2, a3)

    jacobi_res_norm, jacobi_iterations, jacobi_time = SolvingMethods.jacobi(A, n, n, vector_b)
    print(f"Jacobi: {jacobi_iterations} iterations, {jacobi_time} seconds")

    gauss_res_norm, gauss_iterations, gauss_time = SolvingMethods.gauss_seidl(A, n, n, vector_b)
    print(f"Gauss-Seidel: {gauss_iterations} iterations, {gauss_time} seconds")