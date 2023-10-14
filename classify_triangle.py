"""Module contains logic to classify triangle"""


def classify_triangle(a, b, c):
    """
    Method definition: To classify triangle using length of sides
    Input params: a,b,c as length of sides of a triangle
    Output: return type of a triangle as a string

    """
    try:
        if ((type(a) and type(b) and type(c)) is int
            or (type(a) and type(b) and type(c)) is float) and (a > 0 and b > 0 and c > 0):
            # or float # introduce bug -- length of a side of a triangle can also be a float value
            type_of_triangle = "Not a triangle"
            #basic property of triangles
            if (a + b) > c and (b + c) > a and (c+a)>b:
                # Equilateral triangle - lengths of all the three sides are equal
                if a == b and b == c and c == a:
                    type_of_triangle = "Equilateral"

                # Isosceles triangle - lengths of any two sides are equal
                elif a == b or b == c or c == a:
                    type_of_triangle = "Isosceles"

                # Scalene triangle - lengths of all the three sides are different
                else:
                    type_of_triangle = "Scalene"

                # Right Angled - Sum of squares of the lenghts of two sides
                # is equal to the square of the lenght of thrid side
                if ((a**2 + b**2) == c**2) or ((b**2 + c**2) == a**2) or ((a**2 + c**2) == b**2):
                    type_of_triangle = "Right Angled " + type_of_triangle
            return type_of_triangle

        return "Invalid input"
    except ValueError:
        return "Error"
