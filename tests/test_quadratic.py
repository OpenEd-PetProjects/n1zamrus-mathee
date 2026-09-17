import unittest

from quadratic import solve_quadratic


class SolveQuadraticTests(unittest.TestCase):
    def test_returns_two_real_roots(self):
        self.assertEqual(solve_quadratic(1, -3, 2), (1.0, 2.0))

    def test_returns_repeated_root_once(self):
        self.assertEqual(solve_quadratic(1, 4, 4), (-2.0,))

    def test_returns_empty_tuple_without_real_roots(self):
        self.assertEqual(solve_quadratic(1, 0, 1), ())

    def test_supports_linear_equations(self):
        self.assertEqual(solve_quadratic(0, 2, -6), (3.0,))

    def test_rejects_zero_equation(self):
        with self.assertRaises(ValueError):
            solve_quadratic(0, 0, 0)


if __name__ == "__main__":
    unittest.main()
