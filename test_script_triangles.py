"""Module contains testcases for classify triangle logic"""

import unittest
from classify_triangle import classify_triangle


class TestScriptTriangles(unittest.TestCase):
    """Contains testcases as functions for testing classify triangle logic"""

    # test case for equilateral triangle
    def test_equilateral_triangle(self):
        """Positive test case for equilateral triangle"""
        self.assertEqual(
            classify_triangle(1, 1, 1),
            "Equilateral",
            "(1,1,1) is an Equilateral triangle",
        )

    # test case for isosceles triangle
    def test_isosceles_triangle(self):
        """Positive test case for isosceles triangle"""
        self.assertEqual(
            classify_triangle(4, 4, 5), "Isosceles", "(4,4,5) is an Isosceles triangle"
        )

    # test case for scalene triangle
    def test_scalene_triangle(self):
        """Positive test case for scalene triangle"""
        self.assertEqual(
            classify_triangle(7, 8, 9), "Scalene", "(7,8,9) is a Scalene triangle"
        )

    # test case for right angled scalene triangle
    def test_right_scalene_triangle(self):
        """Positive test case for right angled scalene triangle"""
        self.assertEqual(
            classify_triangle(3, 4, 5),
            "Right Angled Scalene",
            "(3,4,5) is a Right Angled Scalene triangle",
        )

    # test case for not a triangle
    def test_not_a_triangle(self):
        """Test case for validating the inputs do not form a triangle"""
        self.assertEqual(
            classify_triangle(2, 2, 5), "Not a triangle", "(2,2,5) is not a triangle"
        )

    # test case - all negative inputs
    def test_neg_int_values(self):
        """Negative test case for equilateral triangle"""
        self.assertNotEqual(
            classify_triangle(-1, -1, -1), "Equilateral", "(-1,-1,-1) is not a triangle"
        )

    # test case for right scalene triangle - to be failed
    # - right angled - when order of the sides is missed
    def test_neg_right_scalene(self):
        """Negative test case for right scalene triangle"""
        self.assertEqual(
            classify_triangle(4, 5, 3),
            "Right Angled Scalene",
            "(4,5,3) is a Right Angled Scalene triangle",
        )

    # test case - to be failed - Isosceles - invalid input string
    def test_neg_invalid_input_str(self):
        """Negative test case for isosceles triangle"""
        self.assertNotEqual(
            classify_triangle(1, 1, "d"),
            "Isosceles",
            "(1,1,d) is an Isosceles triangle",
        )

    # test case - to be failed - Isosceles - invalid input
    def test_neg_invalid_input(self):
        """Negative test case - invalid inputs"""
        self.assertNotEqual(
            classify_triangle(True, ["i", "j"], None),
            "Scalene",
            "(True,['i','j'],None) is an Isosceles triangle",
        )

    # test case - to be failed - Equilateral - Triangle can have sides with length in float values
    def test_neg_equilateral(self):
        """Input values as float"""
        self.assertEqual(
            classify_triangle(1.1, 1.1, 1.1),
            "Equilateral",
            "(1.1,1.1,1.1) is an Equilateral triangle",
        )

    # test case - to be failed - Isosceles - does not satisfy basic triangle property
    def test_neg_isosceles(self):
        """To test basic triangle property"""
        self.assertEqual(
            classify_triangle(2, 5, 2),
            "Not a triangle",
            "(2,5,2) is not a triangle",
        )

    # test case - to be failed - few negative inputs
    def test_neg_int_values_2(self):
        """few negative inputs"""
        self.assertEqual(
            classify_triangle(2, 5, -2), "Invalid input", "(2,5,-2) is not a triangle"
        )


if __name__ == "__main__":
    unittest.main()
