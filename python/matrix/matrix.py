class Matrix:
    """ Given a string representing a matrix of numbers, return the rows and columns of that matrix. """

    def __init__(self, matrix_string):
        """ Compute the number of rows and columns and save the entries of the matrix """
        self.matrix = [list(map(lambda x: int(x), row.split(" "))) for row in matrix_string.split("\n")]

    def row(self, index):
        """ Return a list of the rows, reading each row left-to-right while moving top-to-bottom across the rows """
        return self.matrix[index - 1]

    def column(self, index):
        """ Return a list of the columns, reading each column top-to-bottom while moving from left-to-right """
        return list(list(zip(*self.matrix))[index - 1])