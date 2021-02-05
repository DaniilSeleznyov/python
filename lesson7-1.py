class Matrix:
    def __init__(self, list_1, list_2):
        self.matr = [list_1, list_2]
        self.list_1 = list_1
        self.list_2 = list_2

    def printMatrix_1(self):
        for i in range(len(self.list_1)):
            for j in range(len(self.list_1[i])):
                print(self.list_1[i][j], end=' ')
            print()

    def printMatrix_2(self):
        for i in range(len(self.list_2)):
            for j in range(len(self.list_2[i])):
                print(self.list_2[i][j], end=' ')
            print()

    def __add__(self):
        matr = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

my_matrix = Matrix([[10, 28, 55],
                    [71, 8, 36],
                    [22, 35, 44]],
                   [[68, 24, 17],
                    [9, 11, 88],
                    [27, 15, 91]])

print('\nМатрица 1')
my_matrix.printMatrix_1()
print('\nМатрица 2')
my_matrix.printMatrix_2()
print(f'\nИтоговая матрица \n{my_matrix.__add__()}')
