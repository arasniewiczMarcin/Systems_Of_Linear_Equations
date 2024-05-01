import numpy as np
import math
import time
import copy
from Matrix import Matrix

class SolvingMethods:
    def __init__(self):
        pass

    @staticmethod
    def euclidean_norm(res):
        euclidean_norm = 0
        for value in res.matrix:
            euclidean_norm += value[0]**2

        return math.sqrt(euclidean_norm)


    @staticmethod
    def gauss_seidl(A, n, m, b, max_iterations):
        start = time.time()
        err_norm = 10 ** -9
        f = 8
        x = Matrix(1, n, 0, 0, 0)
        x_new = Matrix(1, n, 0, 0, 0)
        error = 1
        iterations = -1
        res_norm = []
        while error > err_norm and iterations < max_iterations:
            iterations += 1
            for i in range(n):
                sum1 = sum(A.matrix[i][j] * x_new.matrix[j][0] for j in range(i))
                sum2 = sum(A.matrix[i][j] * x.matrix[j][0] for j in range(i + 1, n))
                x_new.matrix[i][0] = (b.matrix[i][0] - sum1 - sum2) / A.matrix[i][i]

            res = A.matmul(x_new)
            res = res - b
            error = SolvingMethods.euclidean_norm(res)
            res_norm.append(error)
            x = copy.deepcopy(x_new)

        stop = time.time()
        gauss_seidl_time = stop - start
        return res_norm, iterations, gauss_seidl_time

    @staticmethod
    def jacobi(A, n, m, b, max_iterations):
        start = time.time()
        err_norm = 10 ** -9
        f = 8
        x = Matrix(1, n, 0, 0, 0)
        x_new = Matrix(1, n, 0, 0, 0)
        error = 1
        iterations = -1
        res_norm = []
        while error > err_norm and iterations < max_iterations:
            iterations += 1
            for i in range(n):
                sum1 = sum(A.matrix[i][j] * x.matrix[j][0] for j in range(i))
                sum2 = sum(A.matrix[i][j] * x.matrix[j][0] for j in range(i + 1, n))
                x_new.matrix[i][0] = (b.matrix[i][0] - sum1 - sum2) / A.matrix[i][i]

            res = A.matmul(x_new)
            res = res - b
            error = SolvingMethods.euclidean_norm(res)
            res_norm.append(error)
            x = copy.deepcopy(x_new)

        stop = time.time()
        jacobi_time = stop - start
        return res_norm, iterations, jacobi_time


    @staticmethod
    def lu_factoring(A, n, m, b):
        start = time.time()
        U = copy.deepcopy(A)
        L = Matrix(n, n, 0, 0, 0)
        for i in range(n):
            L.matrix[i][i] = 1

        for i in range(2, m + 1):
            for j in range(1, i):
                L.matrix[i - 1][j - 1] = U.matrix[i - 1][j - 1] / U.matrix[j - 1][j - 1]
                for t in range(n):
                    U.matrix[i - 1][t] = U.matrix[i - 1][t] - L.matrix[i - 1][j - 1] * U.matrix[j - 1][t]

        x = Matrix(1, n, 0, 0, 0)
        y = Matrix(1, n, 0, 0, 0)
        for i in range(n):
            y.matrix[i][0] = b.matrix[i][0]
            for j in range(i):
                y.matrix[i][0] = y.matrix[i][0] - L.matrix[i][j] * y.matrix[j][0]

        for i in range(n - 1, -1, -1):
            x.matrix[i][0] = y.matrix[i][0]
            for j in range(i + 1, n):
                x.matrix[i][0] = x.matrix[i][0] - U.matrix[i][j] * x.matrix[j][0]
            x.matrix[i][0] = x.matrix[i][0] / U.matrix[i][i]

        res = A.matmul(x)
        res = res - b
        error = SolvingMethods.euclidean_norm(res)
        stop = time.time()
        lu_time = stop - start

        return error, lu_time