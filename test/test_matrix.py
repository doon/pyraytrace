import unittest
import raytracer.base as rt


class TestMatrix(unittest.TestCase):
    def test_matrix(self):
        m = rt.Matrix(
            [
                [1, 2, 3, 4],
                [5.5, 6.5, 7.5, 8.5],
                [9, 10, 11, 12],
                [13.5, 14.5, 15.5, 16.5],
            ]
        )
        self.assertEqual(m[0][0], 1)
        self.assertEqual(m[0][3], 4)
        self.assertEqual(m[1][0], 5.5)
        self.assertEqual(m[3][2], 15.5)

    def test_different_sizes(self):

        m2 = rt.Matrix([[-3, -5], [1, -2]])
        self.assertEqual(m2.size, 2)

        m3 = rt.Matrix([[-3, 5, 0], [1, 2, 0], [0, 1, 1]])
        self.assertEqual(m3.size, 3)

    def test_matrix_multiplication(self):
        m1 = rt.Matrix([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]])

        m2 = rt.Matrix([[0, 1, 2, 4], [1, 2, 4, 8], [2, 4, 8, 16], [4, 8, 16, 32]])
        expected = rt.Matrix(
            [
                [24, 49, 98, 196],
                [31, 64, 128, 256],
                [38, 79, 158, 316],
                [45, 94, 188, 376],
            ]
        )
        self.assertEqual(m1 * m2, expected)

    def test_tuple_multiplication(self):
        m1 = rt.Matrix([[1, 2, 3, 4], [2, 4, 4, 2], [8, 6, 4, 1], [0, 0, 0, 1]])
        t1 = rt.Tuple(1, 2, 3, 1)
        expected = rt.Tuple(18, 24, 33, 1)
        self.assertEqual(m1 * t1, expected)

    def test_identity_matrix(self):
        m1 = rt.Matrix([[0, 1, 2, 4], [1, 2, 4, 8], [2, 4, 8, 16], [4, 8, 16, 32]])
        self.assertEqual(m1 * rt.Matrix.identity(), m1)
        t1 = rt.Tuple(1, 2, 3, 4)
        self.assertEqual(rt.Matrix.identity() * t1, t1)

    def test_transpose(self):
        m1 = rt.Matrix([[0, 9, 3, 0], [9, 8, 0, 8], [1, 8, 5, 3], [0, 0, 5, 8]])
        expected = rt.Matrix([[0, 9, 1, 0], [9, 8, 8, 0], [3, 0, 5, 5], [0, 8, 3, 8]])
        self.assertEqual(m1.transpose(), expected)
        id = rt.Matrix.identity()
        self.assertEqual(id.transpose(), rt.Matrix.identity())
