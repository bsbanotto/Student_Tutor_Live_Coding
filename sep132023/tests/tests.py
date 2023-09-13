#!/usr/bin/env python3
"""
This module contains our test class
"""
import unittest
import functions
import pycodestyle


class Testing(unittest.TestCase):
    """
    Class that will contain all of our test methods
    """
    ## Style Guide Test
    def test_style(self):
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['functions.py'])
        self.assertEqual(result.total_errors, 0, "Found style errors")

    ## Documentation Test
    # Test for Module Documentation
    # Test for Class Documentation
    def test_class_documentation(self):
        self.assertTrue(len(functions.add_ints.__doc__) >= 1,
                        "add_ints function needs documentation")
    # Test for Function Documentation

    ## Integer Addition Tests
    # Test for standard use case
    def test_add_ints(self):
        self.assertEqual(functions.add_ints(2, 3), 5)


    # Test to see if it will add strings
    def test_add_ints1(self):
        with self.assertRaises(TypeError):
            functions.add_ints('Hello', 'there.')

    # Test to see if it will add floats
    def test_add_ints2(self):
        with self.assertRaises(TypeError):
            functions.add_ints(2, 7.8)

    # Test to see if it will add complex numbers
    def test_add_ints3(self):
        with self.assertRaises(TypeError):
            functions.add_ints(4j, 7)

    ## Circle Area Calculation Tests
    # Test to calculate the area of a circle, given integer
    def test_circle_area(self):
        self.assertAlmostEqual(functions.circle_area(3), 7.0685, 3)

if __name__ == "__main__":
    unittest.main()