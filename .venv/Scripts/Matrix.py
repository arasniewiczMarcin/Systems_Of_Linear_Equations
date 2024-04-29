class Matrix:
    #dlugosc wiersza, dlugosc kolumny
    def __init__(self, n, m, a1, a2, a3):
        self.matrix = self.create_matrix(n, m, a1, a2, a3)
        self.n = n
        self.m = m

    def get_n(self):
        return self.n

    def get_m(self):
        return self.m

    def create_matrix(self, n, m, a1, a2, a3):
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            matrix[i][i] = a1
            if i + 1 < n:
                matrix[i][i + 1] = a2
            if i + 2 < n:
                matrix[i][i + 2] = a3
            if i - 1 >= 0:
                matrix[i][i - 1] = a2
            if i - 2 >= 0:
                matrix[i][i - 2] = a3
        return matrix

    #to do
    def __str__(self):
        return '\n'.join([' '.join([str(cell) for cell in row]) for row in self.matrix])

    def matmul(self, other):
        if self.n != other.m:
            print("Can't multiply")
            return

        new_matrix = Matrix(other.n, self.m, 0, 0, 0)
        for i in range(self.n):
            for t in range(other.n):
                for j in range(other.m):
                    new_matrix.matrix[i][t] += self.matrix[i][j] * other.matrix[j][t]

        return new_matrix

    def __sub__(self, other):
        if self.n != other.n or self.m != other.m:
            print("Can't substract")
            return

        new_matrix = Matrix(self.n, self.m, 0, 0, 0)
        for i in range(self.n):
            for j in range(self.m):
                new_matrix.matrix[j][i] = self.matrix[j][i] - other.matrix[j][i]

        return new_matrix

    def assign_values_to_vector(self, values):
        for i in range(self.m):
            self.matrix[i][0] = values[i]
