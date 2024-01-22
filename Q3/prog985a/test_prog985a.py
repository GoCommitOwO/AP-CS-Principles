import random
import unittest
from time import perf_counter as current_time
from prog985a import calc

"""
test each case with the following:
normal - 1, 2
edge - 0, 0
error - 1, -1
"""


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.startTime = current_time()

    def tearDown(self):
        t = current_time() - self.startTime
        print(f"{self.id()}: {t:.6f}")

    def test_add_normal_case(self):
        self.assertEqual(calc.add(1, 2), 3)

    def test_add_edge_case(self):
        self.assertEqual(calc.add(0, 0), 0)

    def test_add_error_case(self):
        self.assertEqual(calc.add(1, -1), 0)

    def test_sub_normal_case(self):
        self.assertEqual(calc.sub(1, 2), -1)

    def test_sub_edge_case(self):
        self.assertEqual(calc.sub(0, 0), 0)

    def test_sub_error_case(self):
        self.assertEqual(calc.sub(1, -1), 2)

    def test_mul_normal_case(self):
        self.assertEqual(calc.mul(1, 2), 2)

    def test_mul_edge_case(self):
        self.assertEqual(calc.mul(0, 0), 0)

    def test_mul_error_case(self):
        self.assertEqual(calc.mul(1, -1), -1)

    def test_div_normal_case(self):
        self.assertEqual(calc.div(1, 2), 0.5)

    def test_div_edge_case(self):
        with self.assertRaises(ZeroDivisionError):
            calc.div(0, 0)

    def test_div_error_case(self):
        self.assertEqual(calc.div(1, -1), -1)

    def test_mod_normal_case(self):
        self.assertEqual(calc.mod(1, 2), 1)

    def test_mod_edge_case(self):
        with self.assertRaises(ZeroDivisionError):
            calc.mod(0, 0)

    def test_mod_error_case(self):
        self.assertEqual(calc.mod(1, -1), 0)





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalc)
    unittest.TextTestRunner(verbosity=0).run(suite)
