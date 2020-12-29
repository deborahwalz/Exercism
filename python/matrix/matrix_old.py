class Matrix:
    """ Given a string representing a matrix of numbers, return the rows and columns of that matrix. """

    def __init__(self, matrix_string):
        """ Compute the number of rows and columns and save the entries of the matrix """
        if matrix_string.find("\n") > 0:
            self.no_rows = matrix_string.count("\n") + 1
            temp = matrix_string[: matrix_string.index("\n")]
            self.no_cols = temp.count(" ") + 1
            matrix = list(matrix_string.replace("\n", " ").split(" "))
        else:
            self.no_rows = 1
            matrix = list(matrix_string.split(" "))
            self.no_cols = len(matrix)
        self.matrix = [int(e) for e in matrix]

    def row(self, index):
        """ Return a list of the rows, reading each row left-to-right while moving top-to-bottom across the rows """
        return self.matrix[self.no_cols * (index - 1): (self.no_cols * (index - 1) + self.no_cols)]

    def column(self, index):
        """ Return a list of the columns, reading each column top-to-bottom while moving from left-to-right """
        return self.matrix[(index - 1): (self.no_cols * (self.no_rows - 1) + index): (self.no_cols)]