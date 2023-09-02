#!/usr/bin/env python3
import unittest
import functions


class Testing(unittest.TestCase):
    def test_add_ints(self):
        self.assertEqual(functions.add_ints(2, 3), 5)

    def test_add_ints1(self):
        with self.assertRaises(TypeError):
            functions.add_ints('Hello, ', 'world!')

    def test_add_ints2(self):
        with self.assertRaises(TypeError):
            functions.add_ints(1.2, 5.9)

    def test_add_ints3(self):
        with self.assertRaises(TypeError):
            functions.add_ints(4j, 6)

    def test_circle_area(self):
        self.assertAlmostEqual(functions.circle_area(3), 7.06858, delta=.001)

if __name__ == "__main__":
    unittest.main()