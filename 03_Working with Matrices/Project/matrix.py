import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):
    """
    Math matrix class

    Attributes:
        g: The data grid
        h: The matrix height
        w: The matrix width

    Important note:
    Determinant and inversion only supported up to a size of 2x2.
    """
    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################

    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise (ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise (NotImplementedError, "Calculating determinant not implemented for matrices larger than 2x2.")


        if self.h == 1:
            return self.g[0][0]
        
        if self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            return a*d - b*c

        return None

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise (ValueError, "Cannot calculate the trace of a non-square matrix.")

        trace = 0.0
        for i in range(self.h):
            trace += self[i][i]

        return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise (ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise (NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        det = self.determinant()



        if self.h == 1:
            inverse = [[1 / det]]

        # 2x2 matrix
        if self.h == 2:
            alpha = self.g[0][0]
            beta = self.g[0][1]
            delta = self.g[1][0]
            gama = self.g[1][1]

            scaler = 1.0 / det

            inverse = [[gama * scaler, -beta * scaler], [-delta * scaler, alpha * scaler]]

        return Matrix(inverse)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """

        mT = []

        nc = self.h
        nr = self.w

        for i in range(nr):
            new = []

            for j in range(nc):
                new.append(self.g[j][i])

            mT.append(new)

        return Matrix(mT)

    def is_square(self):
        """
        Returns if width matches height
        :return: True if the matrix is square
        """
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self, idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self, other):
        """
        Defines the behavior of the + operator

        other: The matrix to be added
        """
        if self.h != other.h or self.w != other.w:
            raise (ValueError, "Matrices can only be added if the dimensions are the same")

        add = []

        for ra, rb in zip(self.g, other.g):
            new = []
            for ca, cb in zip(ra, rb):
                new.append(ca + cb)
            add.append(new)

        return Matrix(add)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """

        neg = []

        for r in self.g:
            new = []
            for c in r:
                new.append(-c)
            neg.append(new)

        return Matrix(neg)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)

        other: The matrix to be subtracted
        """
        sub = []
        if self.h != other.h or self.w != other.w:
            raise (ValueError, "Matrices can only be subtracted if the dimensions are the same")

        for ra, rb in zip(self.g, other.g):
            new = []
            for ca, cb in zip(ra, rb):
                new.append(ca - cb)
            sub.append(new)

        return Matrix(sub)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)

        other: The matrix to be multiplied with.
        """
        mul = []

        bT = other.T()

        if self.w != other.h:   
            raise (ValueError, "Matrices can only be multiplied if the own row count matches the other's column count")

        for ri in range(self.h):
            new = []

            for ci in range(bT.h):
                s = 0.
                for a, b in zip(self.g[ri], bT.g[ci]):
                    s += a * b

                new.append(s)

            mul.append(new)

        return Matrix(mul)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            rmul = []
            for r in self.g:
                new = []
                for c in r:
                    new.append(c*other)
                rmul.append(new)
            return Matrix(rmul)
            