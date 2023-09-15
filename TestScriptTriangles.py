import unittest
from ClassifyTriangle import *

class TestScriptTriangles(unittest.TestCase):

    #test case for equilateral triangle
    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(1,1,1),"Equilateral", "(1,1,1) is an Equilateral triangle")

    #test case for isosceles triangle
    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(4,4,5),"Isosceles", "(4,4,5) is an Isosceles triangle")

    #test case for scalene triangle
    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(7,8,9),"Scalene", "(7,8,9) is a Scalene triangle")

    #test case for right angled scalene triangle
    def test_right_scalene_triangle(self):
        self.assertEqual(classify_triangle(3,4,5),"Right Angled Scalene", "(3,4,5) is a Right Angled Scalene triangle")

    #test case for not a triangle
    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(2,2,5),"Not a triangle", "(2,2,5) is not a triangle")
    
    #test case for right scalene triangle - to be failed - right angled - when order of the sides is missed
    def test_neg_right_scalene(self):
        self.assertEqual(classify_triangle(4,5,3),"Right Angled Scalene", "(3,4,5) is a Right Angled Scalene triangle")

    #test case - to be failed - Isosceles - invalid input string
    def test_neg_invalid_input_str(self):
        self.assertEqual(classify_triangle(1,1,"d"),"Isosceles", "(1,1,d) is an Isosceles triangle")

    #test case - to be failed - Isosceles - invalid input
    def test_neg_invalid_input(self):
        self.assertEqual(classify_triangle(True,["i","j"],None),"Scalene", "(True,['i','j'],None) is an Isosceles triangle")

    #test case - to be failed - Equilateral - Triangle can have sides with length in float values
    def test_neg_equilateral(self):
        self.assertEqual(classify_triangle(1.1,1.1,1.1),"Equilateral", "(1.1,1.1,1.1) is an Equilateral triangle")

    #test case - to be failed - Isosceles - does not satisfy basic triangle property
    def test_neg_isosceles(self):
        self.assertNotEqual(classify_triangle(2,5,2),"Isosceles", "(2,5,2) is not an Isosceles triangle")


if __name__ == "__main__":
    unittest.main()