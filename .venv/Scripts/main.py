#188857 Marcin Araśniewicz
import numpy as np
from Matrix import Matrix
from Solving_Methods import SolvingMethods
from plot import Plot



if __name__ == "__main__":
    e = 8

    n = 957
    a1 = 5 + e
    a2 = a3 = -1
    f = 8
    b = [np.sin(i * (f + 1)) for i in range(n)]

    vector_b = Matrix(1, n, 0, 0, 0)
    vector_b.assign_values_to_vector(b)
    A = Matrix(n, n, a1, a2, a3)

    jacobi_res_norm, jacobi_iterations, jacobi_time = SolvingMethods.jacobi(A, n, n, vector_b, 200)
    print(f"Jacobi: {jacobi_iterations} iterations, {jacobi_time} seconds")

    gauss_res_norm, gauss_iterations, gauss_time = SolvingMethods.gauss_seidl(A, n, n, vector_b, 200)
    print(f"Gauss-Seidel: {gauss_iterations} iterations, {gauss_time} seconds")

    Plot.make_plot_norms(jacobi_iterations, jacobi_res_norm, gauss_iterations, gauss_res_norm)

    #equation number 2
    a1 = 3
    a2 = a3 = -1
    n = 957
    f = 8
    b = [np.sin(i * (f + 1)) for i in range(n)]
    vector_b = Matrix(1, n, 0, 0, 0)
    vector_b.assign_values_to_vector(b)
    A = Matrix(n, n, a1, a2, a3)

    jacobi_res_norm, jacobi_iterations, jacobi_time = SolvingMethods.jacobi(A, n, n, vector_b, 100)
    print(f"Jacobi: {jacobi_iterations} iterations, {jacobi_time} seconds")

    gauss_res_norm, gauss_iterations, gauss_time = SolvingMethods.gauss_seidl(A, n, n, vector_b, 100)
    print(f"Gauss-Seidel: {gauss_iterations} iterations, {gauss_time} seconds")

    Plot.make_plot_norms(jacobi_iterations, jacobi_res_norm, gauss_iterations, gauss_res_norm)

    err, lu_time = SolvingMethods.lu_factoring(A, n, n, vector_b)
    print(f"LU factorization: {lu_time} seconds") 
    print(f"error norm = {err}")

    #equation number 3
    N = [100, 500, 1000, 1500, 2000, 2500]
    jacobi_times = []
    gauss_times = []
    lu_times = []
    for i in N:
        e = 8
        a1 = 5 + e
        a2 = a3 = -1
        f = 8
        b = [np.sin(j * (f + 1)) for j in range(i)]
        vector_b = Matrix(1, i, 0, 0, 0)
        vector_b.assign_values_to_vector(b)
        A = Matrix(i, i, a1, a2, a3)
        jacobi_res_norm, jacobi_iterations, jacobi_time = SolvingMethods.jacobi(A, i, i, vector_b, 200)
        print(f"For N = {i} - Jacobi: {jacobi_iterations} iterations, {jacobi_time} seconds {jacobi_res_norm} ")
        jacobi_times.append(jacobi_time)
        gauss_res_norm, gauss_iterations, gauss_time = SolvingMethods.gauss_seidl(A, i, i, vector_b, 200)
        print(f"For N = {i} - Gauss-Seidel: {gauss_iterations} iterations, {gauss_time} seconds {gauss_res_norm}")
        gauss_times.append(gauss_time)
        err, lu_time = SolvingMethods.lu_factoring(A, i, i, vector_b)
        print(f"For N = {i} - LU factorization: {lu_time} seconds {err}")
        lu_times.append(lu_time)

    Plot.make_plot_comparison(N, jacobi_times, gauss_times, lu_times)
